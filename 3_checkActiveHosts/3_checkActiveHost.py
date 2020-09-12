from scapy.all import *
conf.verb = 0

TIMEOUT = 2

ip_addr = input("Enter Destination IP address(ex.192.168.31.1):")


packet = IP(dst=ip_addr)/ICMP()
# packet.show()

reply = sr1(packet, timeout=TIMEOUT)

if reply is None:
    print(ip_addr, "is DOWN")
else:
    print(ip_addr, "is UP")