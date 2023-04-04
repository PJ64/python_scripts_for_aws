import boto3
import sys

profile = sys.argv[1]
bucket_name = sys.argv[2]

session = boto3.Session(profile_name=profile)

try:
  s3=session.resource("s3")
  bucket = s3.Bucket(bucket_name)
  for obj in bucket.objects.all():
    print(obj.key)
except Exception as e:
  print(e)