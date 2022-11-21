#import scrapy
from bs4 import BeautifulSoup
#from lxml import etree
import requests
import re

#https://www.geeksforgeeks.org/beautifulsoup-search-by-text-inside-a-tag/
#https://www.delftstack.com/howto/python/python-find-all-occurrences-in-string/
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

def link_trasher(url_input,visted_urls):
    '''Takes already visited URL and adds it to do not visit list'''
    visted_urls.append(url_input)

def already_visited_url(visited_urls, potential_url):
    for url in visited_urls:
        if (potential_url == url):
            return True
    return False

def duplicate_link_checker(visited_urls,url_to_visit):
    '''Takes links in upcoming urls to visit, makes sure they have not already been visited,
        then gets returns updated urls to visit list.'''
    for url in url_to_visit:
        if (already_visited_url(visited_urls,url)):
            visited_urls.append(url)


class LinkGatherer:
    urls_to_visit = []
