#!/usr/bin/python

# import libraries
import requests
import re
import urllib.parse as urlparse

# change this value
target_url = '<URL>'
# create an empty list
target_links = []

# query the website and extract content
def extract_links_from(url):
    response = requests.get(url)
    # from the response use regex to extract href
    return re.findall('(?:href=")(.*?)"', response.content.decode())


def crawl(url):
    # from the function extract_links_from setthe value as href_links variable
    href_links = extract_links_from(url)
    # iterate through every element in href_links
    for link in href_links:
        # join the URL and link
        link = urlparse.urljoin(url, link)

# run the function
crawl(target_url)
