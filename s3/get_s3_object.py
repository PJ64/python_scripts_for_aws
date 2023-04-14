import boto3
import sys

profile = sys.argv[1]
bucket_name = sys.argv[2]
object_key = sys.argv[3]

session = boto3.Session(profile_name=profile)

try:
  s3_client=session.client("s3")
  s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key=object_key
    )

  print(s3_object)
except Exception as e:
  print(e)

