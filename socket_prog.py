import socket
import sys
from datetime import datetime

def scan_target(target_host, ports_to_scan):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[!] Could not resolve hostname: {target_host}")
        return

    print("=" * 50)
    print(f"Scanning Target: {target_host} ({target_ip}")
    print(f"Time Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port:<5} : OPEN")
        else:
            print(f"[-] Port {port:<5} : Closed / Filtered")

        s.close()

if __name__ == "__main__":
    target = "127.0.0.1"
    ports = [22, 80, 443, 8080]
    scan_target(target, ports)
