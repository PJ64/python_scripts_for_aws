import boto3
import sys
import datetime

profile = sys.argv[1]
bucket_name = sys.argv[2]

session = boto3.Session(profile_name=profile)

try:
  s3=session.resource("s3")
  bucket = s3.Bucket(bucket_name)

  obj_list = []
  for obj in bucket.objects.all():
    obj_list.append(obj)

  for obj in sorted(obj_list, key=lambda x: x.last_modified, reverse=False):
    print(f'Key: {obj.key}\nLast modified: {obj.last_modified}')
except Exception as e:
  print(e)