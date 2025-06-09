# 📁 Project Part 8

Welcome to the Eighth Project of my DevOps-1 learning journey! 🚀

This branch contains a hands-on project for learning the GitOps concept to manage infrastructure and applications as code

## 🌐 Repository
In this repository, only the essentials are kept to keep it minimal 

You can view the full version at full repository

- DevOps-1_App : https://github.com/TRPMAN/DevOps-1_App.git
- DevOps-1_Infra : https://github.com/TRPMAN/DevOps-1_Infra.git

## 🧱 Stack Used
- Github Action : Pipeline/Workflow
- Terraform : Managing Infrastructure
- Maven : Testing Source Code
- Sonarcloud : Analysis Dashboard
- ECR : Storing Container Image
- EKS : Creating Cluster

## 📚 Step ( App_RE = DevOps-1_App Repository, Infra_RE=DevOps-1_Infra Repository ) 
1. Create App_RE and Infra_RE
2. Create IAM user,S3 and add secret in Infra_RE
3. Write Terraform and Workflow in Infra_RE and test workflow
4. Create ECR and Sonarcloud organization and project then add secret in App_RE
5. Write workflow testing_appin and Buid_And_Publish in App_RE
6. Create Helm Chart from K8ss(in this part, I already do it on Project7_K8s)
7. Write workflow Deploy_To_EKS in App_RE and test workflow
8. Test Website

## 🧠 Problem
Webpage cannot login so I solving this by
- I check mysql pod
  - Command : kubectl get pod, kubectl describe pod mysqlpod
  - Result : It always in pending stage because it waiting for PVC
- I check pvc
  - Command : kubectl get pvc, kubectl describe pvc pvcname
  - Result : It say there is no default storageClassName
- It is because in previous project, I use Kops to create cluster and Kops already create default storageClassName
- So I change my helm template when ever persistence.enabled: false, it should use emptyDir in that node

---
Thanks for visiting! 💡
