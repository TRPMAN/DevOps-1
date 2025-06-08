# About Exercise 1 🚀
This exercise is for learning and practicing how to build a CI/CD pipeline with the following steps:
- Fetch Source Code from a GitHub Repository  
- Build the Artifact using Maven  
- Run Unit Tests with Maven  
- Analyze the Source Code using SonarQube  
- Store the Artifact in Nexus Repository
- Send a Notification to Slack indicating whether the Pipeline execution was SUCCESS or FAILURE

## SonarQube
- SonarQube is running on port 9000, but it's behind Nginx, which proxies it to be accessible via port 80
- SonarQube server starts on EC2 within the same VPC as Jenkins, so it should use a private IP for more security
- Create a Quality Gateway to set conditions
- After creating the Quality Gateway, create a webhook → URL: http://<private ip>:8080/sonarqube-webhook

## Nexus
- Create repository:
  - Group: Both hosted and proxy
  - Hosted: Store artifacts
  - Proxy: Download dependencies
- Like SonarQube, use a private IP to communicate with Jenkins