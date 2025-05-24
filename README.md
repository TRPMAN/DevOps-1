# 📁 Project Part 3

Welcome to the Third Project of my DevOps-1 learning journey! 🚀

This branch is where I work on a hands-on project to re-architect Project 2 using managed AWS service

## 🧱 Stack Used
- Tomcat : Application server
- RabbitMQ : Message Broker
- Memcached : DB Caching
- MySQL : SQL Database

## AWS Service Rearch
- Elastic Beanstalk : Replaces EC2, ASG, and ELB for Tomcat
- Amazon MQ : Replaces RabbitMQ
- ElastiCache : Replaces Memcached
- RDS : Replaces MySQL
- CloudFront : Enables global content delivery

## 📚 Step

1. Create RDS, Amazon MQ, and ElastiCache and Backend Security Group
2. Initialize RDS by connecting and setting up the database
3. Create Elastic Beanstalk to provision EC2, ASG, and ELB for Tomcat service
4. Allow traffic from Beanstalk EC2 in the Backend Security group
5. Build the source code and deploy artifacts to Beanstalk
6. Create a record in GoDaddy pointing to the ELB endpoint
7. Set up CloudFront -> Choose Beanstalk ELB and attach SSL certificate from GoDaddy
8. Access the app via custom domain to verify functionality

---
Thanks for visiting! 💡