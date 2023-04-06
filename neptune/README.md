# Python scripts for Amazon Neptune

### append_gremlin_file.py
Appends records to a gremlin csv file.

**Parameters**

id: unique id for each row.

label: name of the entity type. e.g. person, game, etc.

**Usage**

python .\append_gremlin_file.py *human_x* *person*

---

### s3_neptune_upload.py
Creates or updates, and then uploads a csv file to Amazon S3

**Parameters**

profile_name: name of the AWS profile that you want to authenicate with.

bucket_name: name of the S3 bucket that you want to download and upload to.

file_name: name of the file to create and upload.

id: unique id for each row.

label: name of the entity type. e.g. person, game, etc.

**Usage**

python .\s3_neptune_upload.py *profile_name* *bucket_name* *file_name* *human_x* *person*

---
