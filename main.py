#import scrapy
import link_gatherer
import tree_creator
import tree_creator
from bs4 import BeautifulSoup
#from lxml import etree
import requests
import re

from link_gatherer import LinkGatherer
import info_gatherer


# https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch
# https://www.geeksforgeeks.org/beautifulsoup-object-python-beautifulsoup/
class SpiderMan:

    if __name__ == '__main__':
        urls_to_visit = []
        print (info_gatherer.trim_raw_text(info_gatherer.master_filter('https://callofduty.fandom.com/wiki/Easter_Eggs')))
        #print (info_gatherer.trim_raw_text(info_gatherer.master_filter('https://callofduty.fandom.com/wiki/Wonder_Weapons')))
        link_gatherer.link_getter('https://callofduty.fandom.com/wiki/Easter_Eggs',urls_to_visit)

        root_node = tree_creator.TreeNode("Links")

        tree_creator.TreeNode.print_tree(root_node.build_initial_tree())


