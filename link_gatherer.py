import scrapy
from bs4 import BeautifulSoup
from lxml import etree
import requests
import re


class LinkGatherer:
    webpage = 'https://callofduty.fandom.com/wiki/Easter_Eggs'
    # webpage = 'https://en.wikipedia.org/wiki/Call_of_Duty'
    page_info = requests.get(webpage)
    page_text = page_info.text

    url = 'https://callofduty.fandom.com/wiki/Easter_Eggs'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    # https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
    urls_to_visit = []

    for link in soup.find_all('a'):
        # Get potential link and check start of string for h in http and if found, add to link array
        maybe_link = link.get('href')
        if maybe_link[0] == 'h':
            urls_to_visit.append(link.get('href'))

    print(urls_to_visit)
