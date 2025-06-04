# 📁 Project Part 5

Welcome to the Fifth Project of my DevOps-1 learning journey! 🚀

This branch contains a hands-on project for managing Project1_HostWebsite and containerizing it with Docker

## 🧱 Stack Used
- Nginx    -> 1.27      : Web Service
- Tomcat   -> 10, JDK21 : Application Server
- RabbitMQ -> 4.0       : Message Broker
- Memcache -> 1.6       : DB Caching
- MySQL    -> 8.0.33    : SQL Database

## 🛠️ Tool used
- Maven -> 3.9.9 : Build the artifact
- JDK   -> JDK21 : Maven require JDK

## 🐳 Docker base image
- mysql     : 8.0.33
- memcache  : latest
- rabbitmq  : latest
- tomcat    : 10-jdk21
- nginx     : latest

## 📚 Step
1. Understand all steps to setup all stack service
1. List all the tools,services and versions of project and find base image
2. Write Dockerfile for all stack(Only Memcache and RabbitMQ that they can use official base image)
3. Write Docker-compose file
4. Build and test it
5. Push DockerImage into the Dockerhub

## 🧠 Problem
Webpage cannot login(so the problem will be it cannot connect to database) so I solving this by
- I check containers 
  - Command : docker ps  
  - Result : It do not show the db container
- I check all containers 
  - Command : docker ps -a  
  - Result : Db container is in exited state
- I check is db initialize correctly 
  - Command : docker logs dbcontainer  
  - Result : It show there is no password 
- I check Dockerfile  
  - Result : I saw MYSQL_ROOT_PASSWORD=MYSQL_ROOT_PASSWORD so I fix it
  
It still cannot login so I solving this by
- I check containers 
  - Command : docker ps 
  - Result : It show that db container running correctly
- I want to check inside container 
  - Command : docker exec -it dbcontainer bash
- I want to check db_backupsql 
  - Command : cd docker-entrypoint-initdb.d  
  - Result : It show the db file with correctly data
- I want to check that database is exist 
  - Command : mysql -u root -p accounts
  - Result : It show something like cannot found this database
- I check Dockerfile
  - Result : I see MYSQl_DATABASE spelling mistake so I fix it
  
It still cannot login again so I solving this by
- I want to check inside container 
  - Command : docker exec -it dbcontainer bash
- I want to check that database is exist 
  - Command : mysql -u root -p accounts
  - Result : It show something like cannot found this database
- I think docker compose build do not build the current version so I try to search on internet and AI
  - Result : It say it will not build any new data if you did not remove volume
- I remove all container and all volume, build it and run all container again
  - Command : docker compose down -v
  - Result : After run all container, everything work fine!

---
Thanks for visiting! 💡
