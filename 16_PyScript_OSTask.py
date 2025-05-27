#!/usr/bin/python3
import os
userlist = ["Jenkins","Ansible","Docker","DevOps"]

print("Adding User in System")
print("----------------------------------------")

# Adding User
for user in userlist:
    exitcode = os.system("id {}".format(user))
    # If the previous script is not error, it will return 0
    if exitcode != 0:
        print("User '{}' not added".format(user))
        os.system("useradd {}".format(user))
        print("User '{}' added".format(user))
    else:
        print("User '{}' is already exist".format(user))
    print("----------------------------------------")

# If group is not exists, add it
exitcode = os.system("grep science /etc/group")
if exitcode != 0:
    print("Group science does not exist")
    os.system("groupadd science")
    print("Group science added")
else:
    print("Group science is already exist")
print("----------------------------------------")

# Adding User to group
for user in userlist:
    print("Adding User {} in group".format(user))
    os.system("usermod -g science {}".format(user))
    # If the previous script is not error, it will return 0
print("----------------------------------------")
print("Create Directory in /opt/")
if os.path.isdir("/opt/science"):
    print("Directory '/opt/science' already exists")
else:
    os.mkdir("/opt/science")
    print("Directory '/opt/science' created successfully")
print("----------------------------------------")
print("Assigning permissions and ownership to /opt/science")
os.system("chown :science /opt/science")
os.system("chmod 770 /opt/science")
print("Assigning permissions and ownership success")
print("----------------------------------------")