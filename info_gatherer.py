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
    start_index = 0
    original_index = 0
    index_back = 0
    # Create temporary list with chars to get rid of
    temp = string_to_list_convert(text)
    # iterate through list of characters
    for char in text:
        print(f'Index is currently {index} before anything')
        if char == '=':
            #Check for starting index of equal string

            # if temp[index - 1] == ' ':
            #     #Assign start index value, then increase index until end of string character > reached
            #     start_index = index - 1
            #     while temp[index] != '>':
            #         index = index + 1

            if temp[index - 2] == ' ':
                #Assign start index value, then increase index until end of string character > reached
                start_index = index - 2
                original_index = index
                index_back = 2
                while temp[index] != '>':
                    index = index + 1

            elif temp[index - 3] == ' ':
                #Assign start index value, then increase index until end of string character > reached
                start_index = index - 3
                original_index = index
                index_back = 3
                while temp[index] != '>':
                    index = index + 1

            elif temp[index - 4] == ' ':
                #Assign start index value, then increase index until end of string character > reached
                start_index = index - 4
                original_index = index
                index_back = 4
                print(f'Index is {index} while length of temp is {len(temp)}')
                print(f'temp is {temp[index-1]} {temp[index]} {temp[index+1]}')
                while temp[index] != '>' and index < len(temp):
                    print(f'Index is {index} while length of temp is {len(temp)}')
                    index = index + 1

            elif temp[index - 5] == ' ':
                #Assign start index value, then increase index until end of string character > reached
                start_index = index - 5
                original_index = index
                index_back = 5
                while temp[index] != '>':
                    index = index + 1

            elif temp[index - 6] == ' ':
                #Assign start index value, then increase index until end of string character > reached
                start_index = index - 6
                original_index = index
                index_back = 6
                while temp[index] != '>':
                    index = index + 1

            print(f'Start index is {start_index} end is {index + 1}')
            print(f'Length of temp is {len(temp)}')
            del (temp[start_index: index + 1])
            print(f'New length of temp is {len(temp)}')
            index = index - ((index+index_back) - original_index)
            print(index)
            print("Running")

            # Recalculating index based on new length of set

        index += 1

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
