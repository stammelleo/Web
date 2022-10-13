import scrapy
from bs4 import BeautifulSoup
from lxml import etree
import requests
import re
from link_gatherer import *


class InfoGatherer:

    # Gather string surrounding word Easter
    def easter_text_finder(self, page_text):
        result = [_.start() for _ in re.finditer(' Easter ', page_text)]
        for index in result:
            print(page_text[index - 100: index + 100])
            print('-' * 30)
        result = [_.start() for _ in re.finditer(' easter ', page_text)]
        for index in result:
            print(page_text[index - 100: index + 100])
            print('-' * 30)