# About Exercise 1 🚀
This exercise is for learning and practicing how to build a CI/CD pipeline with the following steps:
- Fetch source code from a GitHub repository
- Build the artifact using Maven
- Run unit tests with Maven
- Analyze the source code using SonarQube
- Store the artifact in Nexus Repository
- Send a notification to Slack indicating whether the pipeline execution was SUCCESS or FAILURE

## SonarQube
- SonarQube Server start on EC2 with same VPC with Jenkins so it should use private ip for more secure
- Create Quality Gateway to make conditions like Bug > 10 -> Fail
- After create Quality Gateway should create Webhoook -> url : http://(private ip):8080/sonarqube-webhook

## Nexus
- Create Repo
  - Group : Both Hosted and Proxy
  - Hosted : Store something like artifact
  - Proxy : Download dependencies
- Like SonarQube use Private IP to communicate with jenkins