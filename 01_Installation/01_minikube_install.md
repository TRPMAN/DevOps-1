# Easy Way to install minikube
Open powershell as administrator and execute below command 

- Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

If getting Error, Turn Off Your Anti Virus for a moment and try again.

Install Minikube with chocolaty, Close powershell and start again with admin

- choco install minikube kubernetes-cli -y
Execute to Setup Minikube cluster
- minikube start

# Minikube Command
- minikube start/stop : start or stop cluster
- minikube delete : delete cluster(and VM that minikube created)
- minikube service <name> --url : print the accessible service URL