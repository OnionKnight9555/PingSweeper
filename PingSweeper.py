import subprocess

def ping(ip):
    result = subprocess.run(
        ["ping", "-c", "3", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        print(ip, "is ONLINE")
    else:
        print(ip, "is OFFLINE")

base = "192.168.1."

for i in range(1, 11):
    ip = base + str(i)
    ping(ip)