import boto3
import sys

profile = sys.argv[1]
bucket_name = sys.argv[2]
file_path = 'vertex_1.csv'

session = boto3.Session(profile_name=profile)

try:
  s3=session.client("s3")
  with open(file_path, 'wb') as f:
    s3.download_fileobj(bucket_name, 'neptune/vertex_1.csv', f)
except Exception as e:
  print(e)