#import scrapy
from bs4 import BeautifulSoup
#from lxml import etree
import requests
import re

#https://www.geeksforgeeks.org/beautifulsoup-search-by-text-inside-a-tag/
#https://www.delftstack.com/howto/python/python-find-all-occurrences-in-string/
def link_getter(webpage,urls_to_visit):
    '''Takes webpage and current list of URL's as parameter and returns list of webpage links on original page'''
    url_error = None
    try:
        reqs = requests.get(webpage)
        soup = BeautifulSoup(reqs.text, 'html.parser')
    except requests.exceptions.InvalidURL as req_error:
        url_error = req_error
        print(req_error)

    if url_error is None:
        for link in soup.find_all('a'):
            # Get potential link and check start of string for h in http and if found, add to link array
            maybe_link = link.get('href')
            if is_actually_link(maybe_link):
                # Checking for https, then turn into http
                if maybe_link[4] == 's':
                    maybe_link = maybe_link[:4] + maybe_link[5:]
                urls_to_visit.append(maybe_link)
                # *********TEST CODE - TEMPORARILY LIMIT SIZE OF URLS TO VISTS**********
                if len(urls_to_visit) > 100:
                    return urls_to_visit
    return urls_to_visit

def is_actually_link(maybe_link):
    '''Checks conditions for being a link, returns True if all are true'''
    if maybe_link != None and len(maybe_link) != 0 and maybe_link[0] == 'h':
        return True
    else:
        return False


