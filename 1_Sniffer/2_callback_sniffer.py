from scapy.all import *

def scapyCallback(pkt):
    pkt.show()

sniff(filter='tcp and port 80', prn=scapyCallback)


# data = sniff(filter='tcp and port 80', count=100)

# for index in range(10):
#     print(data[index].show())
#     print('\n\n')