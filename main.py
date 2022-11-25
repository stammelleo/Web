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
i = 1
class SpiderMan:

    if __name__ == '__main__':
        urls_to_visit = []
        fake_url_to_visit = ['https://en.wikipedia.org/wiki/Main_Page',
                             'https://en.wikipedia.org/wiki/David_(son_of_Heraclius)',
                             'https://en.wikipedia.org/wiki/Avunculate_marriage',
                             'https://en.wikipedia.org/wiki/Marriage']
        depth_counter = 2
        print (info_gatherer.trim_raw_text(info_gatherer.master_filter('https://callofduty.fandom.com/wiki/Easter_Eggs')))
        link_gatherer.link_getter('https://callofduty.fandom.com/wiki/Easter_Eggs',urls_to_visit)
        cod_root_node = tree_creator.TreeNode("https://callofduty.fandom.com/wiki/Easter_Eggs")

        tree_creator.add_all_childen(cod_root_node,urls_to_visit,2)
        cod_root_node.print_tree()

        # while  depth_counter < 3:
        #     depth_counter += 1
        #     cod_root_node.add_to_tree_depth()
        #     cod_root_node.print_tree()
