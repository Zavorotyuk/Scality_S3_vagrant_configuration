import boto
from boto.s3.connection import S3Connection, OrdinaryCallingFormat

connection = S3Connection(
     aws_access_key_id='accessKey1',
     aws_secret_access_key='verySecretKey1',
     is_secure=False,
     port=8000,
     calling_format=OrdinaryCallingFormat(),
     host='localhost'
)

#connection.create_bucket('buck', headers=None, policy=None)

bucket_name = row_input('bucket name -->')
print bucket_name + "BUCKETNAME"
bucket = connection.get_bucket(bucket_name, validate=True)

b = connection.get_bucket(bucket_name)
put_key = row_input('item key -->')
k = b.new_key(put_key)
path_to_file =  row_input('path to file -->')
k.set_contents_from_filename(path_to_file)


for key in bucket.list():
     print "{name}\t{size}\t{modified}".format(
         name = key.name,
         size = key.size,
         modified = key.last_modified,
     )

