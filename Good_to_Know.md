# Terraform Command
- terraform init : initialize a Terraform working directory, download provider plugins and set up backend
- terraform validate : check the configuration files for syntax errors and internal consistency
- terraform plan : create an execution plan showing what actions Terraform will take to reach the desired state
- terraform apply : apply the changes required to reach the desired state of the configuration
- terraform destroy : destroy all resources managed by the current Terraform configuration
- terraform fmt : format Terraform configuration files to a canonical style
- terraform show : display the current state or a plan in a human-readable format
- terraform output : extract and show output variables from the state file

# Extra Command
- aws eks update-kubeconfig --region <region-code> --name <cluster-name> : import .kube/config to your local machine(need to aws configure to the right user)