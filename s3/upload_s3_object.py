import boto3
import sys

profile = sys.argv[1]
bucket_name = sys.argv[2]
file_path = 'vertex.csv'

session = boto3.Session(profile_name=profile)

try:
  s3=session.client("s3")
  response = s3.upload_file(file_path, bucket_name, 'neptune/vertex_1.csv')
  print(response)
except Exception as e:
  print(e)

