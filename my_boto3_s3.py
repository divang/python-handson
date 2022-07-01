import boto3

def list_all_s3_buckets():
	# Let's use Amazon S3
	s3 = boto3.resource('s3')
	# Print out bucket names
	for bucket in s3.buckets.all():
	    print(bucket.name)

def download_from_s3():
	# Downloading file from S3
	s3 = boto3.client('s3')
	s3.download_file('python-hands-on-div26', 'data.csv', 'data-from-s3.csv')

def upload_to_s3():
	s3 = boto3.client('s3')
	with open("data.json", "rb") as f:
	    s3.upload_fileobj(f, "python-hands-on-div26", "data-from-local.json")

#list_all_s3_buckets()
#download_from_s3()
upload_to_s3()
'''
botocore.exceptions.ClientError: An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
'''
