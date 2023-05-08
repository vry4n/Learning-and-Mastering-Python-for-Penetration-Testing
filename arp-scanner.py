# Tool Description: ARP scanner
# Author: Vry4n
# Usage: python3 arp-scanner.py

from scapy.all import Ether,ARP,srp

# Example usage
target_ip = input("Enter an IP/Range, example: 10.10.0.0/16: ")  # Specify the target IP range or a single IP
interface = input("Enter your NIC card name, can be found using ifconfig/ipconfig, example: eth0: ")  # Specify the network interface to use for scanning

def arp_scan(target_ip, interface):
    # Create an Ether object with the destination MAC address set to the broadcast MAC address
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Create an ARP request packet
    arp = ARP(pdst=target_ip)

    # Combine the Ether and ARP packets
    packet = ether / arp

    # Send the packet and capture the response
    result = srp(packet, timeout=3, iface=interface, verbose=0)[0]

    # Process the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

try:
    if len(target_ip) != 0 and len(interface) != 0:
        scan_result = arp_scan(target_ip, interface)
    else:
        print("[-] Warning: enter the target IP and interface.")
except OSError:
    print("[-] Warning: Invalid NIC card. use ifconfig to display the available NIC cards.")

try:
    if scan_result:
        # Print the results
        print("IP\t\t\tMAC Address")
        print("-----------------------------------------")
        for device in scan_result:
            print(f"{device['ip']}\t{device['mac']}")
except NameError:
    print("[-] Warning: Something went wrong.")
