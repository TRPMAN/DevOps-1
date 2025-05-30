# About Exercise 5
This exercise focuses on variable,the priority of variable and gather_facts on Ansible playbook

## Good to Know
#Priority of variable
- Command Line(rarely used) > Inside playbook > host_vars > group_vars > all(only in group_vars)
  - Priority in inventory : hosts > children 
  - Example cli: ansible-playbook -e name=cli learning_vars.yaml
- Have a variable file and want it to high priority
  - Use vars_files and mention file path in playbook

##Gather_facts
- Show the variable that store in gather_facts
  - ansible -m setup web01
- Disable gather_facts by adding this line in playbook 
  - gather_facts: False 
