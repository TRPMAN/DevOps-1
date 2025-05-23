#!/bin/bash

# Variable Declaration
# PACKAGE="httpd wget unzip"
# SVC="httpd"
URL='https://www.tooplate.com/zip-templates/2098_health.zip'
ART_NAME='2098_health'
TEMPDIR="/tmp/webfiles"

## Check if it centos or ubuntu
yum --help &> /dev/null

if [ $? -eq 0 ]
then
  # Set Variable for Centos
  PACKAGE="httpd wget unzip"
  SVC="httpd"

  # Installing Dependencies
  echo "---------------------------------------------------"
  echo "Installing packages"
  echo "---------------------------------------------------"
  sudo yum install $PACKAGE -y > /dev/null
  echo
else
  # Set Variable for Ubuntu
  PACKAGE="apache2 wget unzip"
  SVC="apache2"

  # Installing Dependencies
  echo "---------------------------------------------------"
  echo "Installing packages"
  echo "---------------------------------------------------"
  sudo apt update
  sudo apt install $PACKAGE -y > /dev/null
  echo
fi

# Start & Enable Service
echo "---------------------------------------------------"
echo "Start & Enable HTTPD Service"
echo "---------------------------------------------------"
sudo systemctl start $SVC
sudo systemctl enable $SVC
echo

# Creating Temp Directory and wget webpage in to httpd
echo "---------------------------------------------------"
echo "Starting Artifact Deployment"
echo "---------------------------------------------------"
mkdir -p $TEMPDIR
cd $TEMPDIR
echo

wget $URL > /dev/null
unzip $ART_NAME.zip > /dev/null
sudo cp -r $ART_NAME/* /var/www/html/
echo

# Restart Httpd
echo "---------------------------------------------------"
echo "Restarting HTTPD service"
echo "---------------------------------------------------"
systemctl restart $SVC
echo

# Clean Up
echo "---------------------------------------------------"
echo "Removing Temporary Files"
echo "---------------------------------------------------"
rm -rf $TEMPDIR
echo

sudo systemctl status $SVC
ls /var/www/html/