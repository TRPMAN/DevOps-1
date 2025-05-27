#!/usr/bin/python3
import os
path = "/tmp/test.txt"
if os.path.isfile(path):
    print("It is a File")
elif os.path.isdir(path):
    print("It is a Directory")
else:
    print("It is Empty")