import scrapy
from bs4 import BeautifulSoup
from lxml import etree
import requests
import re

from link_gatherer import LinkGatherer
import info_gatherer


# https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch
# https://www.geeksforgeeks.org/beautifulsoup-object-python-beautifulsoup/
class SpiderMan:

    # occurances = page_text.count(' Easter ')
    # occurances2 = page_text.count('easter')
    # print(occurances, occurances2)

    # LinkGatherer.urls_to_visit


    # result = [i for i in range(len(page_info.text)) if page_info.text.startswith('Easter', i)]

    # print(page_text[141000:142000])

    # print(page_text)

    # BeautifulSoup(file,parser)
    # campbells = BeautifulSoup(page_text, 'lxml')

    if __name__ == '__main__':
        # print(InfoGatherer.easter_text_finder(LinkGatherer.page_text, LinkGatherer.page_text))
        info_gatherer.text_filter(info_gatherer.easter_text_finder(LinkGatherer.page_text))
