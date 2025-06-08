# About Exercise 7
This exercise focuses on template and handlers on Ansible playbook

## Good to Know
#File copy vs template modules
Copy
- Just copies a static file to the destination
- Does not support variables
- Suitable for files that are the same for all hosts

Template
- Can use variables from host_vars, group_vars(So when you want to change the config, just update variable file)
- Checks the destination file before copying — if nothing has changed, it skips the update
- Suitable for dynamic or host-specific configuration files

## Handlers
- Handlers is a kind of task that only runs when it is notified by another task
- It is typically used for actions that should happen only when there is a change