# About Exercise 8
This exercise focuses on using Roles in Ansible Playbooks.

## Good to Know
Tree: displays a directory structure in tree format  
- Install: sudo apt install tree -y
- Use it: tree (path)

Roles: This is a structured way to organize playbooks and related files
- Create a folder for Roles
- Go into that folder and run command: ansible-galaxy init (Roles name)
- Move every Files, Vars, Templates, Tasks, Handlers, etc. into Roles/(Roles name)/
- Roles is smart enough to find Templates or Files so you do not need to pass the directory
  - before src: templates/ntpconf_centos
  - after  src: ntpconf_centos.j2
- Change Template file format to .j2(In the pervious lecture, I forgot to do it)
- Make a change to Playbook to use Roles: 
Tips: You can find any comunity Roles on Ansible-galaxy