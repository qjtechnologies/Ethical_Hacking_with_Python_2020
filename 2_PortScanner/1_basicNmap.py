import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.43.0/24")
# And you would get your results in json
for val in results.keys():
    print(val, results[val],'\n\n')