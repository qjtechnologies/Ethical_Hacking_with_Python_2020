from scapy.all import *

packet = IP()/TCP()
packet.dst = "192.168.31.1"
packet.sport = 22
packet.dport = 25
packet.show()