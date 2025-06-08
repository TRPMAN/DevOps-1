# Helm
In K8s, there are a lot of object file to create like pod, deployment, service, etc.

Helm will acts like a package manager to do templating, minor update, minor changes

So when you create all object file, you put it in to templates

## Command
- helm create <helm-folder-path> : create helm chart
- helm install <release-name> <helm-folder-path> : deploy helm chart
- helm upgrade <release-name> <helm-folder-path> : update helm chart
- helm status <release-name> <helm-folder-path> : status helm chart
- helm uninstall <release-name> <helm-folder-path> : uninstall helm chart

## Option
- -n <namespace> : for specific namespace
  - --create-namespace :  option to create namespace if it is not exist