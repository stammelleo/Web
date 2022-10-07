import scrapy
from bs4 import BeautifulSoup
from lxml import etree
import requests


# https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch
# https://www.geeksforgeeks.org/beautifulsoup-object-python-beautifulsoup/
class SpiderMan:

    webpage = 'https://callofduty.fandom.com/wiki/Easter_Eggs'
    page_info = requests.get(webpage)
    page_text = page_info.text

    # BeautifulSoup(file,parser)
    campbells = BeautifulSoup(page_text, 'lxml')

    print(campbells.prettify())
    tag = campbells.h1

# if __name__ == '__main__':
