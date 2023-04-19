import boto3
import sys

profile = sys.argv[1]
bucket_name = sys.argv[2]
object_key = sys.argv[3]

session = boto3.Session(profile_name=profile)

try:
  s3=session.resource("s3")
  obj = s3.Object(bucket_name, object_key)
  body = obj.get()['Body'].read().decode('utf-8')
  print(body)
except Exception as e:
  print(e)

