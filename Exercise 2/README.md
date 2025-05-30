# About Exercise 2
This exercise focuses on the structure of Ansible playbook .yaml files

## Command
Run a custom task for Ansible
- ansible-playbook -i inventory web_setup.yaml -v 
- ansible-playbook (metion inventory path) (metion .yaml path) (option for log,debug)
  -  --syntax-check : check syntax
  - -C : dry run
  - -v,-vv,-vvv,-vvvv : debug