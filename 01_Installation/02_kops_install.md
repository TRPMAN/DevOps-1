# (Not) Easy way to install Kops
## Steps
- Create EC2 and IAM user with role for awscli
- SSH to instance, install AWS-Cli and attach AWS user
- Install Kops and Kubectl from documentation
- Create S3 and DNS hosted zone with custom domain
- Run the command on instance
- After 10 - 15 Mins, Check kops validate

## Script
- kops create cluster --name=<domain-name> --state=s3://<bucket-name> --zones=us-east-1a,us-east-1b --node-count=2 --node-size=t3.small --control-plane-size=t3.medium --dns-zone=<domain-name> --node-volume-size=12 --control-plane-volume-size=12 --ssh-public-key ~/.ssh/id_ed25519.pub
- kops update cluster --name=<domain-name> --state=s3://<bucket-name> --yes --admin
- kops validate cluster --name=<domain-name> --state=s3://<bucket-name>
- kops delete cluster --name=<domain-name> --state=s3://<bucket-name> --yes

Explanation
- kops create cluster --name=<domain-name> : create cluster on using this domain
- --state=s3://<bucket-name> --zones=us-east-1a,us-east-1b : use this s3 bucket on specific zones
- --node-count=2 : 2 nodes(only worker, not master)
- --node-size=t3.small --control-plane-size=t3.medium : node and control plane ram and cpu
- --dns-zone=<domain-name> : using this dns hosted zone domain
- --node-volume-size=12 --control-plane-volume-size=12 : node and control plane volume(gb)
- --ssh-public-key ~/.ssh/id_ed25519.pub : key path(when we do keygen on master)

## How is it gonna do?
kops.custom.xyz => Godaddy NSRecord => NS server of route53 => api => Masternode