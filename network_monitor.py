import time
import datetime
import json
import speedtest
from ping3 import ping
import socket
import matplotlib.pyplot as plt

"""try:
    import speedtest
    print("speedtest-cli is installed")
except ImportError:
    print("speedtest-cli is NOT installed")

try:
    from ping3 import ping
    print("ping3 is installed")
except ImportError:
    print("ping3 is NOT installed")

try:
    import matplotlib.pyplot as plt
    print("matplotlib is installed")
except ImportError:
    print("matplotlib is NOT installed")"""

def check_ping(host):
    response_time = ping(host)
    return response_time if response_time is not None else -1


def check_dns_resolution(domain):
    start_time = time.time()
    try:
        socket.gethostbyname(domain)
        return time.time() - start_time
    except:
        return -1


def check_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000

    upload_speed = st.upload() / 1_000_000

    return download_speed, upload_speed


def collect_network_data():
    timestamp = datetime.datetime.now().isoformat()

    targets = ["google.com", "amazon.com", "github.com"]

    ping_results = {target: check_ping(target) for target in targets}
    dns_results = {target: check_dns_resolution(target) for target in targets}

    try:
        download_speed, upload_speed = check_speed()
    except:
        download_speed, upload_speed = -1, -1

    network_data = {
        "timestamp": timestamp,
        "ping_ms": ping_results,
        "dns_resolution_s": dns_results,
        "download_speed_mbps": download_speed,
        "upload_speed_mbps": upload_speed
    }

    return network_data


def save_local_json(data, filename="network_data.json"):
    try:
        # Try to load existing data
        with open(filename, 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Append new data
    existing_data.append(data)

    # Save updated data
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=2)


# Main execution
if __name__ == "__main__":
    network_data = collect_network_data()
    save_local_json(network_data)
    print("Network data collected and saved successfully!")
    print(json.dumps(network_data, indent=2))