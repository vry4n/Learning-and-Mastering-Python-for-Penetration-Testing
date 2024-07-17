- [ ] Create subprocess and integrate it with ping Linux command
- [ ] Check if return code is 0 (live host)
	- [ ] result.returncode == 0
- [ ] Create a list & append live hosts to it
- [ ] Create an ipnetwork object to work with subnets
	- [ ] ipaddress.ip_network(network)
- [ ] Capture exceptions
- [ ] Return live hosts
- [ ] Accept user input
- [ ] Run the functions
- [ ] Print the live host list

# Description
An ICMP live host scanner is a network utility used to identify active hosts within a given network range. It leverages the Internet Control Message Protocol (ICMP), a fundamental protocol for network diagnostics, to determine which devices are responding to network traffic.

# Libraries
subprocess
ipaddress
