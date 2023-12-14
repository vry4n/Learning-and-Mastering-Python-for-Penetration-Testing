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
# separate # from links
        if "#" in link:
            link = link.split("#")[0]

# check if the value is already in the list, if not, append the result to the list
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

# run the function
crawl(target_url)
