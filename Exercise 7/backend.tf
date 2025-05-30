terraform {
  backend "s3" {
    bucket = "terraformstate4256"
    key = "terraform/backend"
    region = "us-east-1"
  }
}