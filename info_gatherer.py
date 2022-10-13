import scrapy
from bs4 import BeautifulSoup
from lxml import etree
import requests
import re
from link_gatherer import *


def string_to_list_convert(text):
    # Converts given string to list and returns list
    temp_string = []
    for character in text:
        temp_string.append(character)
    return temp_string


def easter_text_finder(page_text):
    final_string = ''
    result = [_.start() for _ in re.finditer(' Easter ', page_text)]
    for index in result:
        final_string += page_text[index - 100: index + 100]
        print('-' * 30)
    result = [_.start() for _ in re.finditer(' easter ', page_text)]
    for index in result:
        final_string += page_text[index - 100: index + 100]
        print('-' * 30)
    return final_string


def carrot_text_filter(text):
    index = 0
    # Create temporary list with chars to get rid of
    temp = string_to_list_convert(text)
    print(temp)
    temp2 = string_to_list_convert(text)
    start_range = 0
    # iterate through string removing non text
    for char in text:
        if char == '<' and start_range == 0:
            start_range = index
        if char == '>' and start_range != 0:

            print(len(temp))
            print(text[start_range])
            print(text[index])
            print(f'The start range is {start_range} and the end range is {index}')

            del (temp[start_range: index + 1])

            # Recalculating index based on new length of set
            index = index - ((index + 1) - start_range)
            print(len(temp))

            start_range = 0
        index += 1

    # temp 2 should be bigger than temp
    print (len(temp2))
    print(temp2)
    print(temp)
    print(len(temp))
    # iterate through what is left of string list and turn back into string
    # print(f'the text is {temp}')
    # text = ''
    # text.join(str(s) for s in temp)
    # print (f'the text is now {text}')
# class InfoGatherer:

# Gather string surrounding word Easter


# iterate through what is left of string list and turn back into string
# print(f'the text is {temp}')
# text = ''
# text.join(str(s) for s in temp)
# print (f'the text is now {text}')
