# import scapy

# Importing scapy library into our code
from scapy.all import *

data = sniff(filter='tcp and port 80', count=100)

for index in range(10):
    print(data[index].show())
    print('\n\n')