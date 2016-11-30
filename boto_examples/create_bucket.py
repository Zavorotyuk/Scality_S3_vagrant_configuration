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

bucket_name = raw_input('buclet name --> ')
connection.create_bucket(bucket_name, headers=None, policy=None)

for bucket in connection.get_all_buckets():
    print "{name}\t{created}".format(
        name = bucket.name,
        created = bucket.creation_date,
    )
