from fabric.api import *
# Install pip by using script
# wget https://bootstrap.pypa.io/get-pip.py

# fab -l : Show all Func
# feb (func):(arg) : Execute Command
# fab -H (hostname) -u (user) (command) : use -p if you want to use password

def greeting(arg):
    print(f"Hello {arg}")

# local : run command on local
def system_info():
    print("System Information")
    print("----------------------------------------------------")
    print("Disk Space")
    local("df -h")
    print("----------------------------------------------------")
    print("Memory Info")
    local("free -m")
    print("----------------------------------------------------")
    print("System uptime")
    local("uptime")
    print("----------------------------------------------------")

# run : run command on remote machine
# sudo : run command as a sudo
def remote_exec():
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")

    sudo("yum install -y zip unzip wget")

def web_setup(weburl, dirname):
    print("""----------------------------------------------------
Installing web dependencies
----------------------------------------------------""")
    sudo("yum install -y httpd unzip wget")

    print("""----------------------------------------------------
Start & Enable httpd Service
----------------------------------------------------""")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    local("apt install zip unzip -y")

    print("""----------------------------------------------------
Downloading and Pushing Website to Web Server
----------------------------------------------------""")
    # replace %s with weburl
    local(("wget -O website.zip %s") % weburl)
    local("unzip -o website.zip")

    # local cd
    with lcd(dirname):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)

    # remote cd
    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")

    print("Website setup is done.")