import subprocess
import socket
import platform

print("=== WiFi Watcher - White Hat Edition ===")
print("Scanning YOUR network only...\n")

# Get your own IP
hostname = socket.gethostname()
my_ip = socket.gethostbyname(hostname)
print(f"Your device IP: {my_ip}")
print(f"Your hostname: {hostname}\n")

print("Checking devices in ARP table (who talked to your WiFi)...")
try:
    # Works on Linux (your lab) and shows cached devices
    if platform.system() == "Linux":
        result = subprocess.run(["ip", "neigh"], capture_output=True, text=True)
        print(result.stdout)
    else:
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        print(result.stdout)
    
    print("\n--- ANALYSIS ---")
    print("Look at IPs above:")
    print("- 192.168.1.1 = Your Router (normal)")
    print("- Any other 192.168.x.x = Phone/Laptop on your WiFi")
    print("- If you count more devices than you own = POSSIBLE INTRUDER!")
    print("\n🟢 DEFENDER TIP: Change WiFi password if you see unknown device")
    
except Exception as e:
    print(f"Error: {e}")
    print("Try manual: ip neigh")
