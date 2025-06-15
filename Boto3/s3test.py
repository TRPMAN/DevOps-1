#!/usr/bin/env python
import boto3

# create an S3 client
s3 = boto3.client('s3')

# define the bucket name and thr file to upload
bucket_name = 'bucketname'
file_name = input('Enter the path to the file to upload: ')
object_name = 'tests3.txt'

# upload the file to S3
try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
except Exception as e:
    print(f"Error uploading file: {e}")