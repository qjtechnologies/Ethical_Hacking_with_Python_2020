import nmap3
nmap = nmap3.NmapHostDiscovery()
results = nmap.nmap_portscan_only("192.168.43.6")
# print(results.keys())
for ip in results.keys():
    if not (ip == 'runtime' or ip == 'stats'):
        print(ip)
        # print(results[ip])
        host = results[ip][0]['host']
        protocol = results[ip][0]['protocol']
        state = results[ip][0]['state']
        service = results[ip][0]['service']
        print(host,protocol,state,service)