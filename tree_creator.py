# https://www.youtube.com/watch?v=4r_XR9fUPhQ

def add_all_childen(parent,list_of_children):
    '''Adds all links on page as children of parent'''
    for child in list_of_children:
        tree_child = TreeNode(child)
        parent.add_child(tree_child)
        tree_child.parent = parent
    TreeNode.print_tree(parent)


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        '''Adds child node to parent'''
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.name)
        for child in self.children:
            print(child.name)

    def build_initial_tree(self):
        '''Builds starting link tree with games as child nodes'''
        root = self

        cod_links = TreeNode("CODLinks")


        root.add_child(cod_links)


        return root
