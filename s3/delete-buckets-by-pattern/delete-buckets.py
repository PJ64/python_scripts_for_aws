import boto3
import sys, re, json

profile = sys.argv[1]

f = open("patterns.txt", "r")
patterns = f.readlines()

session = boto3.Session(profile_name=profile)
client = session.client('s3')

delete_marker_list = []
version_list = []

try:
  for bucket in (client.list_buckets())["Buckets"]:
    bucket_name = bucket["Name"]
    if re.search('|'.join(patterns),bucket_name, re.IGNORECASE ):

      object_response_paginator = client.get_paginator('list_object_versions')
      for object_response_itr in object_response_paginator.paginate(Bucket=bucket_name):
          # A delete marker in Amazon S3 is a placeholder (or marker) for a versioned object that was named in a simple DELETE request.
          # The following loop creates a list of delete markers to be deleted
          if 'DeleteMarkers' in object_response_itr:
              for delete_marker in object_response_itr['DeleteMarkers']:
                  delete_marker_list.append({'Key': delete_marker['Key'], 'VersionId': delete_marker['VersionId']})

          # Versioning in Amazon S3 is a means of keeping multiple variants of an object in the same bucket
          # The following loop creates a list of versions that need to be deleted
          if 'Versions' in object_response_itr:
              for version in object_response_itr['Versions']:
                  version_list.append({'Key': version['Key'], 'VersionId': version['VersionId']})

      print( f'Removing delete markers from: {bucket_name}' )
      # Iterate the delete marker array and delete the markers
      for i in range(0, len(delete_marker_list), 1000):
          response = client.delete_objects(
              Bucket=bucket_name,
              Delete={
                  'Objects': delete_marker_list[i:i+1000],
                  'Quiet': True
              }
          )
          print(response)

      print( f'Deleting versions from: {bucket_name}' )
      # Iterate the version array and delete the versions
      for i in range(0, len(version_list), 1000):
          response = client.delete_objects(
              Bucket=bucket_name,
              Delete={
                  'Objects': version_list[i:i+1000],
                  'Quiet': True
              }
          )
          print(response)


      print( f'deleting {bucket_name}' )
      # Delete the bucket after it has been cleared
      resp2 = client.delete_bucket( Bucket=bucket_name )
      print("{bucket_name} Successfully deleted: {resp2}")

except Exception as e:
    error_msg = e
    print(error_msg)
