from aws_integration import upload_to_s3
from network_monitor import collect_network_data, save_local_json
from visualization import generate_report
import schedule
import time


def job():
    # Collect and save data
    network_data = collect_network_data()
    save_local_json(network_data)

    # Generate and upload report
    generate_report()


# Run immediately once
job()

# Then schedule to run every hour
schedule.every(1).hour.do(job)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)