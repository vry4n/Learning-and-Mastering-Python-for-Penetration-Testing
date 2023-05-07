import sys
import subprocess
import re

# Accept script parameters
interface = sys.argv[1]  # Replace with your interface name
new_mac = sys.argv[2]  # Replace with the desired MAC address

def change_mac(interace, new_mac):
    print(f"Changing MAC address for {interface} to {new_mac}")

    # Disable the interface
    subprocess.call(["ifconfig", interface, "down"])

    # Change the MAC address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # Enable the interface
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_match = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

    if mac_address_match:
        return mac_address_match.group(0)
    else:
        print("Could not read MAC address.")

current_mac = get_current_mac(interface)
print(f"Current MAC address: {current_mac}")

change_mac(interface, new_mac)

current_mac = get_current_mac(interface)
if current_mac == new_mac:
    print(f"MAC address successfully changed to {current_mac}")
else:
    print("MAC address did not get changed.")
