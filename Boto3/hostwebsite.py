import boto3
import requests
import time

# Configuration
template_name = "tooplate"
region = "us-east-1"  # Change as needed

# Initialize clients
ec2 = boto3.client("ec2", region_name=region)
elbv2 = boto3.client("elbv2", region_name=region)

# 1. Create Key Pair
def create_key_pair(name):
    print(f"Creating key pair '{name}'...")
    key = ec2.create_key_pair(KeyName=name)
    with open(f"{name}.pem", "w") as f:
        f.write(key['KeyMaterial'])
    print(f"Key pair saved to {name}.pem")
    return name

# 2. Create Security Group for EC2
def create_ec2_sg(name, vpc_id, my_ip):
    print(f"Creating EC2 security group '{name}' in VPC {vpc_id}...")
    sg = ec2.create_security_group(
        GroupName=name,
        Description="Allow SSH from my IP and HTTP from anywhere",
        VpcId=vpc_id
    )
    ec2.authorize_security_group_ingress(
        GroupId=sg['GroupId'],
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{ 'CidrIp': f"{my_ip}/32" }]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{ 'CidrIp': "0.0.0.0/0" }]
            }
        ]
    )
    return sg['GroupId']

# 3. Launch EC2 Instance with User Data
def launch_instance(key_name, sg_id, ami_id, subnet_id, user_data):
    print("Launching EC2 instance...")
    resp = ec2.run_instances(
        ImageId=ami_id,
        InstanceType="t2.micro",
        KeyName=key_name,
        SecurityGroupIds=[sg_id],
        SubnetId=subnet_id,
        UserData=user_data,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{ 'Key': 'Name', 'Value': f"{template_name}-instance" }]
        }]
    )
    instance_id = resp['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} launched, waiting for running state...")
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    return instance_id

# 4. Create ALB and Related Resources
def setup_load_balancer(instance_id, vpc_id, subnet_ids):
    grp_name = f"{template_name}-alb-sg"
    print(f"Ensuring ELB security group '{grp_name}' exists...")

    # Check if the security group already exists
    existing_sgs = ec2.describe_security_groups(
        Filters=[
            {'Name': 'group-name', 'Values': [grp_name]},
            {'Name': 'vpc-id', 'Values': [vpc_id]}
        ]
    )['SecurityGroups']

    if existing_sgs:
        elb_sg_id = existing_sgs[0]['GroupId']
        print(f"Security group '{grp_name}' already exists. Using GroupId: {elb_sg_id}")
    else:
        elb_sg = ec2.create_security_group(
            GroupName=grp_name,
            Description="Allow HTTP from anywhere",
            VpcId=vpc_id
        )
        elb_sg_id = elb_sg['GroupId']
        ec2.authorize_security_group_ingress(
            GroupId=elb_sg_id,
            IpPermissions=[{'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}]
        )
        print(f"Created security group '{grp_name}' with GroupId: {elb_sg_id}")

    # Target Group
    print("Creating target group...")
    tg_resp = elbv2.create_target_group(
        Name=f"{template_name}-tg",
        Protocol='HTTP',
        Port=80,
        VpcId=vpc_id,
        TargetType='instance'
    )
    tg_arn = tg_resp['TargetGroups'][0]['TargetGroupArn']

    # Load Balancer
    print("Creating application load balancer...")
    lb_resp = elbv2.create_load_balancer(
        Name=f"{template_name}-alb",
        Subnets=subnet_ids,
        SecurityGroups=[elb_sg_id],
        Scheme='internet-facing',
        Type='application',
        IpAddressType='ipv4'
    )
    lb = lb_resp['LoadBalancers'][0]
    lb_arn = lb['LoadBalancerArn']

    # Register Instance
    print(f"Registering instance {instance_id} to target group...")
    elbv2.register_targets(
        TargetGroupArn=tg_arn,
        Targets=[{'Id': instance_id, 'Port': 80}]
    )

    # Listener
    print("Creating listener for ALB...")
    elbv2.create_listener(
        LoadBalancerArn=lb_arn,
        Protocol='HTTP',
        Port=80,
        DefaultActions=[{ 'Type': 'forward', 'TargetGroupArn': tg_arn }]
    )

    print(f"Load Balancer DNS: {lb['DNSName']}")
    return lb['DNSName']

# Helper: Find latest Amazon Linux 2023 AMI
def get_latest_amazon_linux_2023_ami():
    print("Searching for latest Amazon Linux 2023 AMI...")
    images = ec2.describe_images(
        Filters=[
            {'Name': 'name', 'Values': ['al2023-ami-*-x86_64']},
            {'Name': 'state', 'Values': ['available']}
        ],
        Owners=['137112412989']  # Amazon official AMI account ID
    )['Images']

    if not images:
        raise Exception("No Amazon Linux 2023 AMIs found.")

    # Sort by CreationDate descending
    images.sort(key=lambda x: x['CreationDate'], reverse=True)
    return images[0]['ImageId']


# Main flow
def main():
    # Get default VPC and subnets
    vpcs = ec2.describe_vpcs(Filters=[{'Name':'isDefault','Values':['true']}])['Vpcs']
    vpc_id = vpcs[0]['VpcId']
    subnets = ec2.describe_subnets(Filters=[{'Name':'vpc-id','Values':[vpc_id]}])['Subnets']
    subnet_ids = [s['SubnetId'] for s in subnets]

    # Create key pair
    key_name = create_key_pair(f"{template_name}-key")
    # Create EC2 security group
    my_ip = requests.get("https://checkip.amazonaws.com").text.strip()
    ec2_sg_id = create_ec2_sg(f"{template_name}-sg", vpc_id, my_ip)

    tooplate_url = 'https://www.tooplate.com/zip-templates/2136_kool_form_pack.zip'
    user_data = f"""#!/bin/bash
yum update -y
yum install -y httpd unzip wget
systemctl enable httpd
systemctl start httpd
cd /var/www/html
wget {tooplate_url} -O template.zip
unzip template.zip
folder=$(unzip -Z1 template.zip | head -1 | cut -f1 -d"/")
if [ -d "$folder" ]; then
  mv $folder/* .
  rm -rf $folder
fi
rm template.zip
chown -R apache:apache /var/www/html

systemctl enable amazon-ssm-agent
systemctl start amazon-ssm-agent
"""

    # Find AMI and launch instance
    ami_id = get_latest_amazon_linux_2023_ami()
    instance_id = launch_instance(key_name, ec2_sg_id, ami_id, subnet_ids[0], user_data)

    # Create and configure ALB
    dns = setup_load_balancer(instance_id, vpc_id, subnet_ids)
    print(f"Application Load Balancer endpoint: http://{dns}")

if __name__ == "__main__":
    main()