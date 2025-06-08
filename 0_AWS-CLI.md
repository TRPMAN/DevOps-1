# AWS CLI
Do not need to remember all of AWS CLI but need to know where to find it is a point. https://awscli.amazonaws.com/v2/documentation/api/latest/index.html

## Should create IAM user for ssh into instance
- create IAM user and create access key
- aws configure : insert that IAM user Access and Secret key
- ~/.aws/credentials : credentials storage
- ~/.aws/config : config storage

## Some Example AWS CLI
- aws ec2 run-instances --image-id <ami-Id> --count 1 --instance-type <type> --keyname <keypair-Name> --security-groups <security grp Name>
  - Launch Instance
- aws ec2 terminate-instances --instance-ids <Instance-Id>
  - Terminate Instance
- aws ec2 create-security-group --group-name <security grp Name> --description "<Description>" 
  - Create Security Group
- aws ec2 delete-security-group --group-name <security grp Name>
  - Delete Security Group