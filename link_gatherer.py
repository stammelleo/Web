#import scrapy
from bs4 import BeautifulSoup
#from lxml import etree
import requests
import re

def link_getter(webpage,urls_to_visit):
    '''Takes webpage and current list of URL's as parameter and returns array of webpage links on original page'''
    reqs = requests.get(webpage)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for link in soup.find_all('a'):
        # Get potential link and check start of string for h in http and if found, add to link array
        maybe_link = link.get('href')
        if maybe_link != None:
            if maybe_link[0] == 'h':
                urls_to_visit.append(link.get('href'))

    return urls_to_visit

class LinkGatherer:
    urls_to_visit = []
