variable "region" {
  default = "us-east-1"
}

variable "zone" {
  default = "us-east-1a"
}

variable "amiID" {
  type = map
    default = {
      us-east-1="ami-084568db4383264d4"
      us-east-2="ami-04f167a56786e4b09"
    }
}