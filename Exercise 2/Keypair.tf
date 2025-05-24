resource "aws_key_pair" "dove-key" {
  key_name   = "dove-key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILuWB61HcEQX3Lfk+diGcI65cLSZNlrdMdkc0jdkdTCV milen@LAPTOP-FSMDRTR8"
}

resource "aws_key_pair" "test" {
  key_name   = "test-key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICd0yMqLezaoPTUX/jPDgmIepplhXz6ViBWm/mw4ET3P milen@LAPTOP-FSMDRTR8"
}
