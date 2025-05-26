# Good to Know in Jenkins
Jenkins Document : https://www.jenkins.io/doc/

Jenkins open on port 8080

## Directory
- /var/lib/jenkins : jenkins home directory
- /var/log : jenkins log
- /usr/lib/jvm : java home path (for manual install some tool like JDK)

## Build Trigger
Connect Jenkins with Github
- SSH-keygen, attach public key with github account and private key to jenkins credentials
- Set a Webhook in github : use http://(Jenkins url)/github-webhook/ (select the events you want to trigger builds)
- Go to Jenkins -> Job -> Build Trigger
This section will show some popular build triggers:

### 1.Github hook trigger
Build every time Jenkins gets any event from GitHub (or any event that you selected when setting up the webhook on GitHub)

### 2.Poll SCM
Set the time interval for Jenkins to check changes from the repository. If there are any changes, Jenkins will build the job.

### 3.Build periodically
Set a specific time when Jenkins will automatically build the job.

### 4.Remote Triggers
Create a job URL, token for the user, and CRUMB. This can be used to trigger Jenkins to build via a `curl` command.
- Select Trigger builds remotely (e.g., from scripts) -> Save Job Build url : (JENKINS_URL)/job/Build/build?token=(TOKEN_NAME)
- Go to Jenkins Account -> Security -> API token -> Gen and save Job Token: (Jenkins username):(API_TOKEN)
- Go to Gitbash -> Save CRUMB : wget -q --auth-no-challenge --user (Jenkins username) --password (Jenkins password) --output-document - '(JENKINS_URL)/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'
- Trigger the build with : curl -I -X POST http://(Job token)@(Job Build url) -H "(CRUMB)"

### 5.Build after other projects are built
Build after the choose job has been build

## Security
Good option for Authentication
- Jenkin own user db
- LDAP: For organization-wide authentication

Good option for Authorization
- Matrix-based : Define which groups or users have permission for each action  
- Project-based : Similar to matrix-based, but allows permission control on specific jobs for specific users or groups

Role-based Authorization Strategy
- Good Pulgins for manage security