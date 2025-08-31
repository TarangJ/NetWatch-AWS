# NetWatch-AWS

Python application that monitors network performance, collects data, and uploads it to AWS S3 for storage and analysis. 

# Components

Network Performance Monitor: A Python script that measures:

Ping response times to important servers
Download/upload speeds
Packet loss rates
DNS resolution times
AWS Integration: Store the collected data in AWS S3 and use AWS Lambda for analysis
Visualization: Generate simple reports or graphs of the data

# Clone repository


git clone https://github.com/yourusername/NetWatch-AWS.git
cd NetWatch-AWS

# Install dependencies
pip install -r requirements.txt

python main.py

# AWS Setup Instructions

Create an S3 Bucket:

-Log in to AWS Console
-Go to S3 service
-Create a new bucket named "your-network-monitor-bucket"
-Set appropriate permissions


# Configure AWS Credentials:

-Create an IAM user with S3 access
-Set up AWS credentials on your machine using:
-command: aws configure

-- Enter your Access Key ID, Secret Access Key, region, and output format

-- Optional: Set Up AWS Lambda:

-- Create a Lambda function to process the uploaded data
-- Configure a trigger when new files are uploaded to S3



How to Run the Project

Save the scripts to separate files:

network_monitor.py (main script)
aws_integration.py (S3 functions)
visualization.py (reporting functions)


Main script that ties everything together: main.py
