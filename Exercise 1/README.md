# About Exercise 1
This exercise covers basic Ansible commands and writing a inventory file

## Command
Ansible have a lot of module, so this is a example how to ping to another client machine
- ansible <hostname> -m <module> <mention inventory path>
  - ansible web01 -m ping -i inventory
  - ansible webservers -m ping -i inventory
  - ansible '*' -m ping -i inventory
  - ansible 'web*' -m ping -i inventory

## Remove the footprint asking
Are you sure you want to continue connecting (yes/no/[fingerprint])?

If we login to the client machine for the first time it will ask you this question and how do we remove this?
- Go to the config file : /etc/ansible/ansible.cfg
- Do a command in that file to make a new cfg and save this file for backup
- Edit: host_key_checking=False
- Go to your project directory(inventory and priate key)
- Change permisson private_key file to chmod 400
- Try ansible <hostname> -m ping -i inventory