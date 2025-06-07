module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "3.14.2"

  name = "vprofile-eks"

  cidr = "172.20.0.0/16"
  # this availability zones is given by main.tf
  # slice -> us-east-1a, us-east-1b, us-east-1c or any available at that time
  azs = slice(data.aws_availability_zones.available.names, 0, 3)

  # subnets should have the same as azs
  private_subnets = ["172.20.1.0/24", "172.20.2.0/24", "172.20.3.0/24"]
  public_subnets = ["172.20.4.0/24", "172.20.5.0/24", "172.20.6.0/24"]

  enable_nat_gateway = true
  # nat gateway for 3 private subnets
  single_nat_gateway = true
  enable_dns_hostnames = true

  public_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/elb" = 1
  }

  private_subnet_tags = {
    "kubernetes.io/cluster/${local.cluster_name}" = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}
