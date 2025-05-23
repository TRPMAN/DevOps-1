## For this remote_host
allow ssh to login in ubuntu
vim /etc/ssh/sshd_config
PasswordAuthentication no -> PasswordAuthentication yes
then ssh-keygen
copy pub to target VM : ssh-copy-id (username@hostname)
and you can login with : ssh -i .ssh/id_rsa