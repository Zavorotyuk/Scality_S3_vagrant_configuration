## To run s3

```shell
git clone https://github.com/Zavorotyuk/Scality_S3_vagrant_configuration.git
```
```shell
cd Scality_S3_vagrant_configuration
```
```shell
vagrant up
```
```shell
vagrant ssh
```
```shell
cd S3/
```
```
sudo npm start
```

## awscli

#### About aws configure  
  http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

#### About aws s3api. List of commands and description
  http://docs.aws.amazon.com/cli/latest/reference/s3api/


#### Frequently used commands

Create new bucket
```shell
aws s3api create-bucket --bucket bucket-name
```
Get list of buckets
```shell
aws s3 ls
```
Delete bucket
```shell
aws s3 rb s3://bucket-name --force
```
Copie a local file or S3 object to another location locally or in S3
```shell
aws s3 cp path-to-file s3://bucket-name
```
Get list of objects in bucket-name
```shell
aws s3api list-objects --bucket bucket-name
```



## boto

boto is a python interface to Amazon Web Services

###### Repository https://github.com/boto/boto
###### Documentation http://boto.cloudhackers.com/en/latest/#getting-started

#### Intalation

###### Install via pip:
```shell
$ pip install boto
```

###### Install from source:
```shell
$ git clone git://github.com/boto/boto.git
$ cd boto
$ python setup.py install
```
