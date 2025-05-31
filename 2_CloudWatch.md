# CloudWatch
This sevice is a monitoring service for AWS resources and applications. You can create metrics, dashboards, and alarms for services like EC2, RDS,and more

## For EC2 Example
- Create Alarm and select EC2 instance
- Select Metric like CPUUtilization and set the conditions
- Select noti for SNS topic(group of people for sending noti)
- Select Action like if it in alarm -> Terminate This Instance
- Add name and description

## EC2 Log
This is a exercise for logging from EC2 instance by using S3,EC2 and CloudWatch service
- Create Role form IAM (S3 access, CloudWatchLog access)
- Attach role to the target instance
- Install awslogs in instance
- Create a new configuration info for the logs : /etc/awslogs/awslogs.conf
- Restart and enable awslogs service
- Check the logs in CloudWatch and try some experiments
  - Create some metric
  - Upload to S3 Bucket

This is a exercise for logging from ELB by using S3,EC2 and CloudWatch service
- Edit S3 bucket policy to allow from ELB
- Create target group from the previous EC2 instance and create ELB
- Go to ELB -> Attributes and enable logs -> Choose your S3 bucket
- Check the logs in CloudWatch