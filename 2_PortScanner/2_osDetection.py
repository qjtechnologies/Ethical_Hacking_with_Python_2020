import nmap3
nmap = nmap3.Nmap()
os_results = nmap.nmap_os_detection("192.168.43.1") # MOST BE ROOT
print(os_results)