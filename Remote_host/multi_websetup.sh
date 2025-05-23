#!/bin/bash

USR="devops"

for host in $(cat remhosts)
do 
  echo "-----------------------------------"
  echo "Connecting to $host"
  echo "Pushing Script to $host"
  scp websetup.sh $USR@$host:/tmp/
  echo "Execute .sh"
  ssh $USR@$host sudo /tmp/websetup.sh
  ssh $USR@$host sudo rm -rf /tmp/websetup.sh
  echo "-----------------------------------"
done