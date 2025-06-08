## For this remote_host
allow ssh to login in ubuntu
- vim /etc/ssh/sshd_config
  - PasswordAuthentication no -> PasswordAuthentication yes
- ssh-keygen : genarate public and private key
- ssh-copy-id <username>@<hostname> : copy pub to target VM 
- ssh -i .ssh/id_rsa : login to target VM
