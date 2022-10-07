import scrapy
from bs4 import BeautifulSoup
from lxml import etree
import requests
import re


# https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch
# https://www.geeksforgeeks.org/beautifulsoup-object-python-beautifulsoup/
class SpiderMan:
    # webpage = 'https://callofduty.fandom.com/wiki/Easter_Eggs'
    webpage = 'https://en.wikipedia.org/wiki/Call_of_Duty'
    page_info = requests.get(webpage)
    page_text = page_info.text

    url = 'https://callofduty.fandom.com/wiki/Easter_Eggs'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        print(link.get('href'))
        urls.append(link.get('href'))

    occurances = page_text.count(' Easter ')
    occurances2 = page_text.count('easter')
    print(occurances, occurances2)

    # result = [i for i in range(len(page_info.text)) if page_info.text.startswith('Easter', i)]
    result = [_.start() for _ in re.finditer(' Easter ', page_text)]
    print(result)
    for index in result:
        print(page_text[index - 100: index + 100])
        print('-' * 30)

    # print(page_text[141000:142000])

    # print(page_text)

    # BeautifulSoup(file,parser)
    campbells = BeautifulSoup(page_text, 'lxml')

    # print(campbells.prettify())
    tag = campbells.findAll('Easter')
    # print(tag)

    # go through the whole webpage looking for string easter
    # for line in campbells.findAll(content=True):
    #   print(line)
# if __name__ == '__main__':
