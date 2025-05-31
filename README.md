# 📁 Project Part 4

Welcome to the Forth Project of my DevOps-1 learning journey! 🚀

This branch contains a hands-on project for hosting a web application using AWS CodePipeline

## 🧱 Tools Used
- Bitbucket : Source code repository

## 🛠️ AWS Service
- Elastic Beanstalk : Host and manage the web application
- S3 : Store Artifacts
- RDS : Host the MySQL database
- CodeBuild : Build the application (install dependencies, compile)
- CodePipeline : Automate the CI/CD workflow

## 📚 Step

1. Create S3 Bucket,Beanstalk and RDS
2. Initialize RDS by connecting and setting up the database
3. Create Bitbucket, attach key and migrate source code from Github to Bitbucker  
4. Create and configuration Amazon CodeBuild
5. Create a pipeline with Amazon CodePipeline
6. Attach policy to Amazon CodePipeline Role
7. Just test it

## 🧠 Problem
- Cannot install maven with wget so I decided to download it on local and copy it to S3 then fetch from that S3

---
Thanks for visiting! 💡
