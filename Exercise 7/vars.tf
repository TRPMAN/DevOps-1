variable "region" {
  default = "us-east-1"
}

variable "zone" {
  default = "us-east-1a"
}

variable "webuser" {
  default = "ubuntu"
}
variable "amiID" {
  type = map
    default = {
      us-east-1="ami-084568db4383264d4"
      us-east-2="ami-04f167a56786e4b09"
    }
}

variable "ZONE1" {
  default = "us-east-2a"
}

variable "ZONE2" {
  default = "us-east-2b"
}

variable "ZONE3" {
  default = "us-east-2c"
}