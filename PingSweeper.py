# Imports
import subprocess
import ipaddress
import time
import sys

def ping(ip):
    result = subprocess.run(
        ["ping", "-c", "3", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

# Ask the user for input
network_input = input("Enter the Network + CIDR Notation (e.g. 192.168.1.0/24): ")

# Parse the network
network = ipaddress.ip_network(network_input, strict=False)

print(f"Scanning {network}", end="")
for i in range(5):
    time.sleep(0.5)
    print(".", end="")
    sys.stdout.flush()

print() #move to next line

print(f"Total hosts to scan: {network.num_addresses}\n")

online = []
offline = []

for ip in network.hosts():
    ip_str = str(ip)
    if ping(ip_str):
        online.append(ip_str)
        print(ip_str, "ONLINE")
    else:
        offline.append(ip_str)
        print(ip_str, "OFFLINE")

print(" --- Scan Complete ---")
print(f"Online: {len(online)}")
print(f"Offline: {len(offline)}")
print("\nOnline Devices:")
for ip in online:
    print(" -", ip)
