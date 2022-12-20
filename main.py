#import scrapy
import link_gatherer
import tree_creator
from bs4 import BeautifulSoup
#from lxml import etree
import requests
import re

# from link_gatherer import LinkGatherer
import info_gatherer


# https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch
# https://www.geeksforgeeks.org/beautifulsoup-object-python-beautifulsoup/
depth_counter = 4
class SpiderMan:

    if __name__ == '__main__':
        urls_to_visit = []

        #print (info_gatherer.trim_raw_text(info_gatherer.master_filter('https://callofduty.fandom.com/wiki/Easter_Eggs')))

        link_gatherer.link_getter('https://callofduty.fandom.com/wiki/Easter_Eggs',urls_to_visit)
        cod_root_node = tree_creator.TreeNode("https://callofduty.fandom.com/wiki/Easter_Eggs")
        tree_creator.links_in_tree.append(cod_root_node.name)


        tree_creator.add_all_childen(cod_root_node,urls_to_visit,depth_counter)

        for link in tree_creator.links_in_tree:
            print(info_gatherer.trim_raw_text(info_gatherer.master_filter(link)))

