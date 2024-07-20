# Import the socket module, which provides networking capabilities in Python
import socket

# Define the port_scanner function that takes two arguments:
# - target_host: The hostname or IP address of the target.
# - target_ports: A list of port numbers to scan.
def port_scanner(target_host, target_ports):
  # Initialize an empty list to store the open ports found
  open_ports = []

  # Iterate through each port in the target_ports list
  for port in target_ports:
    # Create a TCP socket using socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # The 'with' statement is used to ensure the socket is properly closed after use
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      # Set a timeout of 1 second for the socket using sock.settimeout(1)
      # This prevents the script from hanging on unresponsive ports
      sock.settimeout(1)

      # Attempt to connect to the target host on the current port using sock.connect_ex((target_host, port))
      # sock.connect_ex returns 0 if the connection is successful, otherwise an error code
      result = sock.connect_ex((target_host, port))

      # If the connection is successful (result == 0), append the port to the open_ports list
      if result == 0:
        open_ports.append(port)

  # Return the list of open_ports found
  return open_ports

# Example usage:
# Set the target_host to an example IP address
target_host = "192.168.0.1"  # Replace with your target host

# Define the target_ports as a range from 1 to 1024
target_ports = range(1, 1025)  # Scan ports 1 to 1024

# Call the port_scanner function to perform the scan and store the result in open_ports
open_ports = port_scanner(target_host, target_ports)

# Print the list of open ports found on the target_host
print(f"Open ports on {target_host}: {open_ports}")
