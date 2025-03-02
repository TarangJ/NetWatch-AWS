import boto3
import json
import matplotlib.pyplot as plt

def generate_report(data_file="network_data.json"):
    """Generate a simple report from collected data"""
    with open(data_file, 'r') as f:
        data_points = json.load(f)

    # Extract timestamps and speeds
    timestamps = [dp["timestamp"] for dp in data_points]
    download_speeds = [dp["download_speed_mbps"] for dp in data_points]
    upload_speeds = [dp["upload_speed_mbps"] for dp in data_points]

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, download_speeds, label="Download (Mbps)")
    plt.plot(timestamps, upload_speeds, label="Upload (Mbps)")
    plt.xlabel("Time")
    plt.ylabel("Speed (Mbps)")
    plt.title("Network Speed Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig("network_performance.png")
    print("Report generated: network_performance.png")

    # Optionally upload the report to S3
    def upload_to_s3(file_name, bucket_name, object_name):
        s3 = boto3.client("s3")
        try:
            s3.upload_file(file_name, bucket_name, object_name)
            return True
        except Exception as e:
            print(f"S3 Upload Failed: {e}")
            return False

    if upload_to_s3("network_performance.png", "mynetbucketproj", "reports/latest_report.png"):
        print("Report uploaded to S3 successfully")