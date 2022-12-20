import link_gatherer
import main

##ASK ABOUT BIOSHOCK

# https://www.youtube.com/watch?v=4r_XR9fUPhQ

links_gathered = []
links_in_tree = []
def add_all_childen(parent,list_of_children,depth_count):
    '''Adds all links on page as children of parent'''
    # If bottom of tree, go back up
    if depth_count <= 0:
        return
    else:
        # Counter for tracking list index
        counter = -1

        # Make duplicate list of children to manipulate to avoid errors in future for loops
        variable_list_of_children = make_duplicate_list(list_of_children)

        # If link is already nodes children, get rid of it, else add to list of nodes collected
        for child in variable_list_of_children:
            counter += 1
            if depth_count != 4 and link_already_gathered(child):
                list_of_children.remove(child)
            else:
                links_gathered.append(child)

        # Add children to tree and recursively call method on children
        for child in list_of_children:
            new_urls_to_visit = []
            tree_child = TreeNode(child)
            parent.add_child(tree_child)
            tree_child.parent = parent
            links_in_tree.append(child)
            add_all_childen(tree_child, link_gatherer.link_getter(child,new_urls_to_visit), depth_count - 1)

        print(f'The depth is {depth_count}')
        parent.print_tree()
        print('-------------------------------')
    # print(f'The parent node is {TreeNode.print_tree(parent)}')


def make_duplicate_list(list):
    '''Makes copy of list passed in and returns it'''
    returning_list = []
    for child in list:
        returning_list.append(child)

    return returning_list



def link_already_gathered(child):
    '''Checks if link has already been seen in tree'''
    for link in links_gathered:
        if child == link:
            return True
    return False

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

