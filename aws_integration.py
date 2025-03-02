import datetime
import boto3
from botocore.exceptions import NoCredentialsError
from network_monitor import collect_network_data, save_local_json


def upload_to_s3(local_file, bucket_name, s3_file_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(local_file, bucket_name, s3_file_name)
        return True
    except NoCredentialsError:
        print("AWS credentials not available")
        return False


def update_network_monitor():
    network_data = collect_network_data()

    save_local_json(network_data)Installation

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    s3_filename = f"network_data_{timestamp}.json"

    bucket_name = "yourBucketName" #replace
    if upload_to_s3("network_data.json", bucket_name, s3_filename):
        print(f"Successfully uploaded to S3: {s3_filename}")
    else:
        print("Failed to upload to S3")

# Schedule this function to run periodically
