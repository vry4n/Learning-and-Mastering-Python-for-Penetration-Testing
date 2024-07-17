#!/user/bin/python3

import subprocess # Used to execute external commands (ping in this case)
import ipaddress # Used to validate and work with IP network addresses.

def scan_network(network): #  (IP address and mask)
  try:
    network = ipaddress.ip_network(network) # Validates the network input using ipaddress.ip_network.
  except ValueError:
    print(f"Invalid network address: {network}")

  live_hosts = []
  for host in network.hosts(): # Iterates through the hosts within the specified network range using network.hosts().
    try:
      # Use subprocess to execute the ping command
      result = subprocess.run(["ping", "-c", "1", str(host)], capture_output=True, text=True) # Executes the ping command with -c 1 (send one packet) using subprocess.run.
      if result.returncode == 0: # Checks the return code of the ping command. A return code of 0 indicates success (host is live).
        live_hosts.append(str(host)) # Appends the live host's IP address to the live_hosts list.
    except Exception as e:
      print(f"Error pinging {host}: {e}")

  return live_hosts # Returns the list of live_hosts.

# Example usage:
network_range = input("Enter the network address and mask: ") # Sets a network_range variable.
live_hosts = scan_network(network_range) # Calls the scan_network function to scan the range.

print(f"Live hosts on {network_range}:")
for host in live_hosts: # Prints the live hosts found.
  print(host)
