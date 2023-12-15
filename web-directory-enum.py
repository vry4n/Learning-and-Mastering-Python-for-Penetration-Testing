#!/usr/bin/python

import requests
import os

# Replace 'http://example.com' with the target website URL
base_url = "https://vk9-sec.com"

# Replace 'wordlist.txt' with the path to your wordlist file
wordlist_path = "../../wordlist.txt"

def enumerate_files(base_url, wordlist):
    for word in wordlist:
        # contruct the path
        url = f"{base_url}/{word}" + "/"
        # request using HEAD method looking for return code
        response = requests.head(url)
        # if the code 
        if response.status_code == 200:
            print(f"File found: {url}")

# Check if the wordlist file exists
if os.path.exists(wordlist_path):
    # read the file
    with open(wordlist_path, "r") as file:
        # iterate through each line
        wordlist = [line.strip() for line in file.readlines()]

    # Call the function to enumerate files
    enumerate_files(base_url, wordlist)
