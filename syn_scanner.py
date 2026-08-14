from scapy.all import IP, TCP, sr1, logging
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def syn_scan(target_ip, ports):
    print(f"--- Starting TCP SYN Scan on {target_ip} ---")

    for port in ports:
        ip_layer = IP(dst=target_ip)
        tcp_layer = TCP(dport=port, flags="S")
        packet = ip_layer / tcp_layer

        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
           print(f"[-] Port {port:<5} : Filtered (No Response)")

        elif response.haslayer(TCP):
            if response[TCP].flags == "SA":
                print(f"[+] Port {port:<5} : OPEN")

                rst_pkt = IP(dst=target_ip) / TCP(dport=port, flags="R")
                sr1(rst_pkt, timeout=1, verbose=0)

            elif "R" in str(response[TCP].flags):
                print(f"[-] Port {port:<5} : Closed")

if __name__ == "__main__":
    target = "127.0.0.1"
    ports_list = [22, 80, 443, 8080]

    syn_scan(target, ports_list)
