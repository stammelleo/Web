#import scrapy
from bs4 import BeautifulSoup
#from lxml import etree
import requests
import re
from link_gatherer import *


def text_gatherer(webpage):
    '''Returns unfiltered text on webpage'''
    page_info = requests.get(webpage)
    page_text = page_info.text
    return page_text

def master_filter(url_link):
    '''Calls all filters on incoming raw html, then returns completely filtered readable text'''
    return easter_text_finder(double_space_filter(angle_bracket_filter(equal_sign_filter(html_syntx_filter(carrot_text_filter(
             text_gatherer(url_link)))))))
    # return trim_raw_text(double_space_filter(angle_bracket_filter(equal_sign_filter(html_syntx_filter(carrot_text_filter(
    #     text_gatherer(url_link)))))))

def trim_raw_text(raw_text):
    return raw_text[5500:len(raw_text) - 4500]

def double_space_filter(string):
    '''Filters out double spaces from string parameter'''
    index = 0
    for char in string:
        if char == ' ' and string[index + 1] == ' ':
            string = string[:index] + string[index + 1:]
            index -= 1
        index += 1
    return string

def angle_bracket_filter(string):
    '''Filters out > key from string parameter'''
    index = 0
    for char in string:
        if char == '>':
            string = string[:index] + string[index + 1:]
            index -= 1
        index += 1
    return string

def equal_sign_filter_process(text):
    '''This function takes a text parameter and removes text around = signs'''
    index = 0
    start_index = 0
    end_index = 0
    num_quotes = 0
    for char in text:

        if char == '=':
            start_index = index
            #Searches spots next to equal sign until it find a space, then set start index
            while text[start_index] != ' ':
                start_index -= 1
            #Once the second quote had been reached, set end index and return string with chunk taken out
            while num_quotes < 2:
                if text[index] == '"':
                    num_quotes += 1
                    if num_quotes == 2:
                        end_index = index
                        return text[:start_index + 1] + text[end_index + 1:]
                index += 1
        index += 1

def string_has_equal_sign(raw_string):
    '''Checks if string has equal sign. Returns True if it does'''
    for char in raw_string:
        if char == '=':
            return True
    return False

def equal_sign_filter(raw_text):
    '''Calls equal sign filter repeatedly on text unitl there are none left'''
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


#I got the easter word finder loop from https://www.delftstack.com/howto/python/python-find-all-occurrences-in-string/
def easter_text_finder(page_text):
    '''Searches through text, finding first occurance and final occurance of Easter or easter, then gathers all text
        between those occurances'''
    final_string = ''
    counter = 0
    absolute_lowest_index = 0
    absolute_highest_index = 0
    uppercase_result = [_.start() for _ in re.finditer(' Easter ', page_text)]
    lowercase_result = [_.start() for _ in re.finditer(' easter ', page_text)]
    #If the words easter and Easter appear ten or more times, take page info
    if (len(uppercase_result) + len(lowercase_result) >= 10):
        for index in uppercase_result:
            if (counter == 0):
                absolute_lowest_index = index
                absolute_highest_index = index
            if (index > absolute_highest_index):
                highest_index = index
            counter += 1

        counter = 0
        for index in lowercase_result:
            if (counter == 0 and index < absolute_lowest_index):
                absolute_lowest_index = index
            if (index > absolute_highest_index):
                absolute_highest_index = index
            counter += 1
    #If keywords did not show up enough, return empty string
    else: return ''
    #Gets closer to top and bottom of text based on earliest and latest occurance of Easter and easter, then returns
    #all text between the two points
    a_lowest_fraction = int(absolute_lowest_index - absolute_lowest_index*.97)
    a_highest_fraction = int(absolute_highest_index + absolute_highest_index/4)
    final_string += page_text[a_lowest_fraction:a_highest_fraction]
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
