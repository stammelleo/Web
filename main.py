#import scrapy
import link_gatherer
from bs4 import BeautifulSoup
#from lxml import etree
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
        print(info_gatherer.master_filter('https://callofduty.fandom.com/wiki/Easter_Eggs'))
        #0123lmnopqrststuff
        #Look for equal sign
        #When found, increment to left until space is discovered, call this left slice index
        #Increment pointer to right until right angle bracket is discovered
        #Mark this as right slice index
        #New string = old string[:leftIndex] + old string[rightindex+1:]


        #print(info_gatherer.equal_sign_fiter('dying from the time limit iw-disambig"say either'))

        link_gatherer.link_getter('https://callofduty.fandom.com/wiki/Easter_Eggs',urls_to_visit)
        # print(urls_to_visit)
