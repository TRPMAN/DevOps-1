# Elastic File System(EFS)
This service is a shared file system.It like a EBS but it can use on multiple EC2 instance at the same time

This is the document : https://docs.aws.amazon.com/efs/latest/ug/using-amazon-efs-utils.html

## Using it with accesspoint
- Create EFS and EFS-SG in EFS service
  - allow EC2 instance into inbound rule with type NFS
- Create Accesspoint
- SSh into EC2 instance
- install amazon-efs-util
- vi /etc/fstab
  - <file-system-id> <efs-mount-point> efs _netdev,tls,accesspoint=<access-point-id> 0 0
- mount -fav : if it error or success it gonna show after this command