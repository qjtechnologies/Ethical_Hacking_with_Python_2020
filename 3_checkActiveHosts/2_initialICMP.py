from scapy.all import *


TIMEOUT = 2


packet = IP(dst="192.168.31.2")/ICMP()
packet.show()
# send(packet)

reply = sr1(packet, timeout=TIMEOUT)
reply.show()