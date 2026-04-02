import subprocess

def ping(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        print(ip, "is ONLINE")
    else:
        print(ip, "is OFFLINE")

ping("8.8.8.8")