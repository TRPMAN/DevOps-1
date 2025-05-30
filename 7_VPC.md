# VPC
The concept is something like a local network that you can design all of that

## Fisrt Exercies
Creating VPC with this information
- Region: us-west-1
- VPC Range: 172.20.0.0/16(Enable DNS hostnames)
- 4 Subnets: 2 Public(need to Enable auto-assign public IPv4 address) and 2 Private
  - 172.20.1.0/24 -> Public subnet(us-west-1a)
  - 172.20.2.0/24 -> Public subnet(us-west-1b)
  - 172.20.3.0/24 -> Private subnet(us-west-1a)
  - 172.20.4.0/24 -> Private subnet(us-west-1b)
- 2 Zones: us-west-1a, us-west-1b (I use 1b and 1c because 1a is not available at the moment)
- 1 Internet Gateway
- 2 NAT Gateway
- 2 Elastic ip(for NAT gateway)
- 2 Route Tables: 1 Public and 1 Private
- 1 Bastion host in Public Subnet
  - Create security group and key pair
  - Launch EC2 instance for Bastion host
    - It Must use the AMI that are well tested for the security vulnerabilities in real time
  - Create key pair for private instance
  - Store key pair in Bastion host by using command: scp -i
- Network Access Control List(similar to security group in EC2)
- 1 More VPC for VPC Peering
  - Create VPC in another region
  - Create peering connection
    - Select another region and give vpc-id that you want to make a peering
  - Go into another region and accept peering connection 
  - Make sure to edit Route Tables to make them able to communicate(give the ip range and choose peering connection)

## Second Exercise
Creating VPC wtih Terraform

I save .tf file in Terraform Branch

## Good to Know
Private IP Ranges
- Class A: 10.0.0.0    - 10.255.255.255
- Class B: 172.16.0.0  -  172.31.255.255
- Class C: 192.168.0.0 -    192.168.255.255

Subnet Mask: It shows which part of the IP address is for the network and which is for the host
- IP           172.16.12.3
- Subnet Mask  255.255.0.0/16
- First IP     172.16.0.0 -> For network
- Last IP      172.16.255.255 -> For broadcast
- Usable IP    172.16.0.1 - 172.16.255.254

VPC Public Subnet connect to Internet Gateway

VPC Private Subnet connect to Nat Gateway

Route Table is used to determine how network traffic is directed

You can connect to your instance in VPC private subnet by using VPN or Bastion Host