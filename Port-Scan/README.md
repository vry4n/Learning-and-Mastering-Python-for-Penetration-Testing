- [ ] Define the port_scanner function that takes two arguments:
	- [ ] target_host: The hostname or IP address of the target.
	- [ ] target_ports: A list of port numbers to scan.
- [ ] Initialize an empty list to store the open ports found
- [ ] Iterate through each port in the target_ports list
- [ ] If the connection is successful (result == 0), append the port to the open_ports list
- [ ] Print the list of open ports found on the target_host
# Description
A port scanner is a software tool or script designed to determine which ports on a target host (such as a computer, server, or network device) are open and listening for incoming connections. Ports are virtual entry points through which network services communicate with each other. Each port is associated with a specific service or application, and they are identified by unique numbers ranging from 0 to 65535.
# Libraries
socket
