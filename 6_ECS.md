# Amazon ECS
Amazon ECS is an Elastic Container service for launching containers used with CI/CD

## Cluster
Create new Cluster
- Infrastructure
  - AWS Fargate : AWS will handle compute resource but no maintenance
  - EC2 instance : Create ASG to manage capacity
  - External instance : Add existing compute resources to ECS
- Monitor
  - Container Insights : ECS will collect all metrics in CloudWatch and show the data
 
## Task
 Create Task
 - Task Role: Need to give access to ECS — for example, if ECS uses CloudWatch, the task role should have CloudWatch permissions attached
 - Container: Make sure to map the container port to match the app — for example, if Tomcat listens on port 8080, the container port should be set to 8080 too

## Amazon ECR
Amazon ECR is an Elastic Container Registry service for sharing, storing, and deploying containers with Amazon ECS
