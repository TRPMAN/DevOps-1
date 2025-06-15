import boto3
import time
import os

template_name = "tooplate"
region = "us-east-1"

ec2 = boto3.client("ec2", region_name=region)
elbv2 = boto3.client("elbv2", region_name=region)

def delete_ec2_instance():
    print("Deleting EC2 instance...")
    instances = ec2.describe_instances(
        Filters=[{
            'Name': 'tag:Name',
            'Values': [f"{template_name}-instance"]
        }]
    )['Reservations']
    instance_ids = [i['InstanceId'] for r in instances for i in r['Instances']]
    if instance_ids:
        ec2.terminate_instances(InstanceIds=instance_ids)
        print(f"Waiting for instance(s) to terminate: {instance_ids}")
        waiter = ec2.get_waiter('instance_terminated')
        waiter.wait(InstanceIds=instance_ids)
    else:
        print("No matching EC2 instances found.")

def delete_key_pair():
    key_name = f"{template_name}-key"
    print(f"Deleting key pair '{key_name}'...")
    try:
        ec2.delete_key_pair(KeyName=key_name)
    except Exception as e:
        print(f"Error deleting key pair: {e}")
    try:
        os.remove(f"{key_name}.pem")
    except FileNotFoundError:
        pass

def delete_security_groups():
    print("Deleting security groups...")
    sgs = ec2.describe_security_groups()['SecurityGroups']
    for sg in sgs:
        # Never delete the default security group
        if sg['GroupName'] == 'default':
            continue
        if sg['GroupName'].startswith(f"{template_name}-"):
            try:
                print(f"Deleting SG: {sg['GroupId']} ({sg['GroupName']})")
                ec2.delete_security_group(GroupId=sg['GroupId'])
            except Exception as e:
                print(f"  Could not delete SG {sg['GroupId']}: {e}")

def delete_load_balancer():
    print("Deleting ALB, listener, and target group...")
    lbs = elbv2.describe_load_balancers()['LoadBalancers']
    for lb in lbs:
        if lb['LoadBalancerName'] == f"{template_name}-alb":
            lb_arn = lb['LoadBalancerArn']

            # Delete listeners
            listeners = elbv2.describe_listeners(LoadBalancerArn=lb_arn)['Listeners']
            for listener in listeners:
                elbv2.delete_listener(ListenerArn=listener['ListenerArn'])

            # Delete load balancer
            elbv2.delete_load_balancer(LoadBalancerArn=lb_arn)
            print("Waiting for load balancer deletion...")
            time.sleep(15)  # ALB deletion takes time

            # Delete target group
            tgs = elbv2.describe_target_groups()['TargetGroups']
            for tg in tgs:
                if tg['TargetGroupName'] == f"{template_name}-tg":
                    elbv2.delete_target_group(TargetGroupArn=tg['TargetGroupArn'])

            print("ALB and related resources deleted.")
            return
    print("No matching ALB found.")

def main():
    delete_ec2_instance()
    delete_key_pair()
    delete_load_balancer()
    delete_security_groups()
    print("✅ Cleanup complete.")

if __name__ == "__main__":
    main()