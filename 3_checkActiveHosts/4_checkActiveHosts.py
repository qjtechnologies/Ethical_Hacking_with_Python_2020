from scapy.all import *
conf.verb = 0

TIMEOUT = 1

ip_addr = input("Enter Destination IP address/ IP Range(ex.192.168.31.1-50):")
# ip_addr = "192.168.43.20-60"
print("Range to Scan:",ip_addr)
ip_addr_splitted = ip_addr.split(".")
# print(ip_addr_splitted)
# print(ip_addr_splitted[-1])
ip_addr_splitted_host = ip_addr_splitted[-1].split("-")
# print(ip_addr_splitted_host)

for host in range (int(ip_addr_splitted_host[0]),int(ip_addr_splitted_host[1])+1):
    ip_address = ip_addr_splitted[0]+"."+ip_addr_splitted[1]+"."+ip_addr_splitted[2]+"."+str(host)
    # print(ip_address)
    packet = IP(dst=ip_address)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if reply is None:
        print(ip_address, "is DOWN")
    else:
        print(ip_address, "is UP")

# packet = IP(dst=ip_addr)/ICMP()
# # packet.show()

# reply = sr1(packet, timeout=TIMEOUT)

# if reply is None:
#     print(ip_addr, "is DOWN")
# else:
#     print(ip_addr, "is UP")