#import scrapy
from bs4 import BeautifulSoup
#from lxml import etree
import requests
import re
from link_gatherer import *


def text_gatherer(webpage):
    '''Returns unfiltered text on webpage'''
    webpage = 'https://callofduty.fandom.com/wiki/Easter_Eggs'
    # webpage = 'https://en.wikipedia.org/wiki/Call_of_Duty'
    page_info = requests.get(webpage)
    page_text = page_info.text
    return page_text


def equal_sign_filter_process(text):
    '''This function takes a text parameter and removes text around = signs'''
    index = 0
    start_index = 0
    end_index = 0
    num_quotes = 0
    for char in text:

        if char == '=':
            start_index = index
            while text[start_index] != ' ':
                start_index -= 1

            while num_quotes < 2:
                if text[index] == '"':
                    num_quotes += 1
                index += 1
            end_index = index
        index += 1
    print(text[start_index:end_index+1])
    print('----------------------------')
    return text[:start_index] + text[end_index + 1:]
def string_has_equal_sign(raw_string):
    for char in raw_string:
        if char == '=':
            return True
    return False

def equal_sign_filter(raw_text):
    while string_has_equal_sign(raw_text):
        raw_text = equal_sign_filter_process(raw_text)
    return raw_text


def html_syntx_filter(text):
    '''Takes a string parameter and returns that string with &#160; stripped'''
    index = 0
    # Create temporary list with chars to get rid of
    temp = string_to_list_convert(text)
    # iterate through list of characters
    for char in text:
        if char == '&':
            # Deleting <&#160;> from strings
            del (temp[index: index + 6])

            # Recalculating index based on new length of set
            index = index - 6
            start_range = 0

        index += 1

    return list_to_string_convert(temp)

def string_to_list_convert(text):
    '''Converts string parameter to a list'''
    # Converts given string to list and returns list

    temp_string = []
    for character in text:
        temp_string.append(character)
    return temp_string


def list_to_string_convert(bucket):
    '''Converts a list parameter to a string'''
    r_string = ''
    # iterate through given list adding to string
    for item in bucket:
        r_string += item
    return r_string



def easter_text_finder(page_text):
    '''Searches through text, Finding text around words Easter and easter'''
    final_string = ''
    result = [_.start() for _ in re.finditer(' Easter ', page_text)]
    for index in result:
        final_string += page_text[index - 600: index + 500]
        print('-' * 30)
    result = [_.start() for _ in re.finditer(' easter ', page_text)]
    for index in result:
        final_string += page_text[index - 600: index + 500]
        print('-' * 30)
    return final_string


def carrot_text_filter(text):
    '''Filters out junk in text between <...> strings'''
    index = 0
    # Create temporary list with chars to get rid of
    temp = string_to_list_convert(text)
    start_range = 0
    # iterate through string removing non text
    for char in text:
        if char == '<' and start_range == 0:
            start_range = index
        elif char == '>' and start_range != 0:
            # Deleting <...> from strings
            del (temp[start_range: index + 1])

            # Recalculating index based on new length of set
            index = index - ((index + 1) - start_range)
            start_range = 0
        index += 1



    return list_to_string_convert(temp)

# class InfoGatherer:

# Gather string surrounding word Easter


# iterate through what is left of string list and turn back into string
# print(f'the text is {temp}')
# text = ''
# text.join(str(s) for s in temp)
# print (f'the text is now {text}')
