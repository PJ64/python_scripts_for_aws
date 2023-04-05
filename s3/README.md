# Python scripts for Amazon S3

### download_s3_object.py
Downloads a object from an Amazon S3 bucket.
**Note**: You should run the **upload_s3_object.py** script first.

**Parameters**

profile_name - name of the AWS profile that you want to authenicate with.

bucket_name - name of the S3 bucket that you want to download from.

**Usage**

python .\download_s3_object.py *profile_name* *bucket_name*

---
### list_s3_objects.py'
Prints a list of all the objects in an S3 Bucket.

**Parameters**

profile_name - name of the AWS profile that you want to authenicate with.

bucket_name - name of the S3 bucket that you want to list the objects in.

**Usage**

python .\list_s3_objects.py *profile_name* *bucket_name*

---

### list_s3_objects_date_sorted.py
Prints a sorted list of all the objects in an S3 Bucket, from oldest to newest by the last modified date.

**Parameters**

profile_name - name of the AWS profile that you want to authenicate with.

bucket_name - name of the S3 bucket that you want to list the objects in.

**Usage**

python .\list_s3_objects_date_sorted.py *profile_name* *bucket_name*

---

### put_s3_object.py
Puts an object into an Amazon S3 bucket.

**Parameters**

profile_name - name of the AWS profile that you want to authenicate with.

bucket_name - name of the S3 bucket where you want to put an object.

**Usage**

python .\put_s3_object.py *profile_name* *bucket_name*

---

### upload_s3_object.py
Uploads and object to an Amazon S3 bucket.

**Parameters**

profile_name - name of the AWS profile that you want to authenicate with.

bucket_name - name of the S3 bucket that you want to upload too.

**Usage**

python .\upload_s3_object.py *profile_name* *bucket_name*

