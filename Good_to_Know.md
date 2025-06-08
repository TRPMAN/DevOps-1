# Good to Know
Commands on K8s are too hard to remember all of it, so you should always use the documentation

This is some basic command and you can go to Kubectl Cheat Sheet for more useful command

## Useful Command and Option
Command
- kubectl create -f <file.yaml> : create object using .yaml file(for one time create)
- kubectl apply -f <file.yaml> : create(if it does not have) or update resource base on file.yaml detail
- kubectl edit <object> <object-name> : edit object(rarely use case)
- kubectl delete <object> <object-name> : delete object
- kubectl run <object-name> --image=<image-name> : create pod(mostly use to test)
- kubectl get <object> <object-name> : show all obejct
- kubectl describe <object> <object-name> : More infomation from specific object(for monitoring, troubleshooting)
- kubectl create <object> <object-name> --image=<image-name> --dry-run=client -o yaml > <file-name>.yaml : to create default .yaml file(for exam)

Option
- -n <namespace> : metion specific namespace
- --all-namespaces : all namespaces(mostly use on get, describe)
- -o <wide, yaml, anyformat> : get more detail or specific format(mostly use on get)
- --watch : watching change

## Config
config file contain cluster information, so that why kubectl know the cluster detail
- .kube/config : cluster detail
  - in context will told you cluster: <cluster-name> should use by this user: <user-name>
- kubectl config view : show the context

## Namespace(ns)
Namespace use to manage when you have more projects, more users and it is not good to do anything inside default namespace
- kubectl get all <namespace> : show all objects on that namespace
  - --all-namespaces : show all objects on all namespaces
- kubectl delete ns <namespace> : delete EVERYTHING in namespace

## Pod
A Pod is the smallest unit in Kubernetes that runs one(mostly one container) or more containers inside it
- kubectl logs <pod-name>: Output of container that execute command
- kubectl exec --stdin --tty <pod-name> -- /bin/<sh-bash> : login inside pod

## Service(svc)
It similar to LoadBalancer. Pod need to destory and recreate everytime we update so it will not have a static ip that why it need a service that have a static ip infront of them to communicate.

There are 3 service
- NodePort : Use for export pod to outside network(not production usecase)
- ClusterIP : For internal communication
- LoadBalancer : Use for export pod to outside network(production usecase)

## Replica set(rs)
Replica will try to create pod to match the number that you metion. It can recrate pod for you if it fail or even if it is in another node
- kubectl scale --replicas=<num> <replicaset-name> : change the scaling number(not production usecase)

## Deployment(deploy)
It is simialr to Replica Set but it will mostly use on deploy because it can manage all pod and rs
- kubectl rollout status deployment/<deployment-name> : show current deployment status
- kubectl rollout history deployment/<deployment-name> : show all version and history
- kubectl rollout undo deployment/<deployment-name> : rollback to previous verison
  - --to-revision=<num> : rollback to the version

## Volume
In DevOps, we usually don't manage Kubernetes volumes directly, but we should define them in manifests

## Persistent Volumes Claims(pvc)
It is the volumes that we create before mount it and it will not got deleted even if the pods got delete

## ConfigMaps(cm)
Config Maps is collection of variables and you can inject variable into pod

## Secrets
Similar to ConfigMaps, but it stores the data in an encoded(base64) format(so do not use this type in real-time)

## Ingress
Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster 

It acts like an Elastic Load Balancer with routing rules that determine how to direct traffic to the appropriate services

Ingress Controller must be installed in the cluster before using it
- Install Controller -> Apply Deployment -> Apply Sevice -> Create DNS Cname Record -> Apply Ingress

## DaemonSet(ds)
DaemonSet is mostly for collecting logs and monitoring nodes

## Tains & Toleration
Taints and tolerations work together to control which pods can be scheduled on specific nodes
- kubectl taint nodes <node> <key>=<value>:<effect> : taint to a node

## Limit
Maximum CPU and memory a pod can use to reduce noisy neighbor issues

## Jobs
Jobs is similar to pods but it run for a specific period of time

## Lens
Monitoring Dashboard for k8s cluster