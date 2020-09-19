from scapy.all import *
conf.verb = 0

src_ip = "192.168.2.2"
dst_ip = "192.168.31.1"

for port in range(1,100):
    pkt = IP(src = src_ip, dst=dst_ip)/TCP(dport=port)
    # print(pkt)
    send(pkt, iface="wlan0")
    print(f"Packet Sent from {src_ip} to {dst_ip} on port {port}")

# pkt.show()


# Assignment
# Syntax: python3 ip_spoofing.py <src_ip_range> <destination_ip> <port-range>
# Example: python3 ip_spoofing.py 192.168.3.2-100 192.168.31.1 1-10