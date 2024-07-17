import boto3
import os

# AWS credentials and region
aws_access_key_id = 'access_key'            # Replace the given access key
aws_secret_access_key = 'secret_key'        # Replace the given secret key
region_name = 'us-east-1'

# Set S3 bucket and file path
bucket_name = 'bucket_name'                 # Replace the given bucket name
file_path = 'TEST_03.xml'                   
file_name = os.path.basename(file_path)

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Upload file to S3 with SSE-S3 Encryption
try:
    s3.upload_file(file_path, bucket_name, file_name, ExtraArgs={'ServerSideEncryption': 'AES256'})
    print(f'File uploaded successfully to {bucket_name}/{file_name,}')
except Exception as e:
    print(f'Error uploading file: {e}')
#