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
        urls_to_visit = []
        test_array = ['A','B','C','D','E','F','G']
        # print(InfoGatherer.easter_text_finder(LinkGatherer.page_text, LinkGatherer.page_text))
        text1 = info_gatherer.carrot_text_filter(info_gatherer.easter_text_finder(info_gatherer.text_gatherer('https://callofduty.fandom.com/wiki/Easter_Eggs')))
        # print(info_gatherer.equal_sign_fiter(text1))
        text2 = info_gatherer.html_syntx_filter(text1)
        # print(text2)
        #print(info_gatherer.equal_sign_filter('dying from the time limit iw-disambig" title="Brutus">Brutussay either'))
        print(info_gatherer.equal_sign_filter('0123 5="789a" dgf="cdefghij">lmnopqrst stuff="otherstuff"> morestuff="evenmore"> stuff'))
        #0123lmnopqrststuff
        #Look for equal sign
        #When found, increment to left until space is discovered, call this left slice index
        #Increment pointer to right until right angle bracket is discovered
        #Mark this as right slice index
        #New string = old string[:leftIndex] + old string[rightindex+1:]


        #print(info_gatherer.equal_sign_fiter('dying from the time limit iw-disambig"say either'))

        link_gatherer.link_getter('https://callofduty.fandom.com/wiki/Easter_Eggs',urls_to_visit)
        i = 0
        for char in test_array:
            print(char)
            print(test_array[i])
            if (char == 'C'):
                del (test_array[i])
            print(f'New index is {test_array[i]}')
            i += 1
        print(test_array)
        # print(info_gatherer.equal_sign_fiter(text2))
        # print(urls_to_visit)
