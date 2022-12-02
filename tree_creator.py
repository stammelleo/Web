import link_gatherer
import main


# https://www.youtube.com/watch?v=4r_XR9fUPhQ

def add_all_childen(parent,list_of_children,depth_count):
    '''Adds all links on page as children of parent'''
    if depth_count <= 0:
        return
    else:
        for child in list_of_children:
            # urls_to_visit = ['https://en.wikipedia.org/wiki/Main_Page',
            #                  'https://en.wikipedia.org/wiki/David_(son_of_Heraclius)',
            #                  'https://en.wikipedia.org/wiki/Avunculate_marriage',
            #                  'https://en.wikipedia.org/wiki/Marriage']
            new_urls_to_visit = []
            tree_child = TreeNode(child)
            parent.add_child(tree_child)
            tree_child.parent = parent
            add_all_childen(tree_child, link_gatherer.link_getter(child,new_urls_to_visit), depth_count - 1)
        parent.print_tree()
        print('-------------------------------')
    # print(f'The parent node is {TreeNode.print_tree(parent)}')


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.visted = False

    def mark_as_visted(self):
        self.visted = True

    def add_child(self, child):
        '''Adds child node to parent'''
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        '''Prints parent node and immediate children'''
        print(self.name)
        integer = 0
        for child in self.children:
            integer += 1
            print(child.name)

    def add_to_tree_depth(self):
        '''Loop to add '''
        for node in self.children:
            # Clear urls to add for each parent
            urls_to_be_added = []
            # Saving name (URL) of node
            name_of_node = node.name
            # Gather links from page and add URLs as children of node
            link_gatherer.link_getter(name_of_node, urls_to_be_added)
            add_all_childen(node,urls_to_be_added)
            print(f'The {node} is a parent of {node.children} END OF CHILDREN')

    def build_initial_tree(self):
        '''Builds starting link tree with games as child nodes'''
        root = self

        cod_links = TreeNode("CODLinks")


        root.add_child(cod_links)


        return root
