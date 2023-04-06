"""
Creates or updates, and then uploads a csv file to Amazon S3

The module is used to create or update, and then upload vertex.csv file to Amazon S3, with purpose of the file being ingested into Amazone Neptune.

Created: April 4th, 2023
"""

#imports
import boto3, sys, csv, os
from botocore.errorfactory import ClientError

# arguments
profile = sys.argv[1]
bucket_name = sys.argv[2]
file_name = sys.argv[3]
id = sys.argv[4]
label = sys.argv[5]

# variables
session = boto3.Session(profile_name=profile)
s3=session.client("s3")

# functions
def download_s3_object():
  try:
    s3.head_object(Bucket=bucket_name, Key=f'neptune/{file_name}')
    with open(file_name, 'wb') as f:
      s3.download_fileobj(bucket_name, f'neptune/{file_name}', f)
  except ClientError as e:
      print(f'Object does not exist: neptune/{file_name}')


def append_gremlin_file():
  try:
    # open with 'a' appends rows to a file
    with open(file_name, 'a', encoding='UTF8',newline='') as f:
      writer = csv.writer(f)
      if os.stat(file_name).st_size == 0: #check if the file is empty and does not have headers
        header = ['~id', '~label']
        writer.writerow(header)

      data = [id, label]
      writer.writerow(data)
  except Exception as e:
    print(e)


def upload_s3_object():
  try:
    s3.upload_file(file_name, bucket_name, f'neptune/{file_name}')
    os.remove(file_name)
  except ClientError as e:
    print(e)


# main
download_s3_object()
append_gremlin_file()
upload_s3_object()