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

def equal_sign_fiter(text):
    '''This function takes a text parameter and removes text around = signs'''
    index = 0
    index_minus_one = 0
    index_minus_two = 0
    index_minus_three = 0
    index_minus_four = 0
    index_minus_five = 0
    index_minus_six = 0
    # Create temporary list with chars to get rid of
    temp = string_to_list_convert(text)
    # iterate through list of characters
    for char in text:
        if char == '=':

            #del (temp[index: index + 6])
            print("Running")

            # Recalculating index based on new length of set
            #index = index - 6

        #Keep a list of recently visited chars in order to find start, which is the space key before start of string
        index += 1
        if index > 0:
            index_minus_one = index - 1
        if index > 2:
            index_minus_two = index - 2
        if index > 3:
            index_minus_three = index - 3
        if index > 4:
            index_minus_four = index - 4
        if index > 5:
            index_minus_five = index - 5
        if index > 6:
            index_minus_six = index - 6


    return list_to_string_convert(temp)
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
            print("Running")

            # Recalculating index based on new length of set
            index = index - 6
            start_range = 0
            print(f"This is {index}")
        print(index)
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
