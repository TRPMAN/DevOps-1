# 📁 Project Part 2

Welcome to the Second Project of my DevOps-1 learning journey! 🚀

This branch is where I work on a hands-on project to Lift & Shift Project 1 to AWS after learning core AWS services

## 🧱 Stack Used
- Tomcat : Application server
- RabbitMQ : Message Broker
- Memcached : DB Caching
- MySQL : SQL Database

## 🛠️ AWS Service
- EC2 : Host 4 Instance (Tomcat, RabbitMQ, Memcached and Mysql)
- ASG : Auto Scaling Group for the Tomcat Instance
- ELB : Used as a load balancer
- ACM : SSL certificate for securing a custom domain (from GoDaddy)
- S3 : Store and deploy web artifacts
- Route 53 : Interval Backend Connection(Mysql, RabbitMQ and Memcached)

## 📚 Step

1. Create SG for ELB, Backend and Tomcat Instance
2. SSH into each instance and install Tomcat, RabbitMQ and Memcached
3. Go into Route53 service -> Created Hosted Zone and Create record for Backend Internal Connection
4. Build source code, store and deploy web artifacts
5. Create ELB and attach ACM
6. Create a record in GoDaddy pointing to the ELB endpoint
6. Create ASG
7. Access the app via Custom Purchased Domain from Godaddy to verify everything works

---
Thanks for visiting! 💡
