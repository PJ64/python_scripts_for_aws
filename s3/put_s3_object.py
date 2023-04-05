import boto3
import sys

profile = sys.argv[1]
bucket_name = sys.argv[2]

session = boto3.Session(profile_name=profile)

try:
  _binary_data = b'string of binary data'

  s3=session.resource("s3")
  object = s3.Object(bucket_name, 'neptune/vertex_2.csv')
  object.put(
    Body=_binary_data
    )

except Exception as e:
  print(e)

