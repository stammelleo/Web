# https://www.youtube.com/watch?v=4r_XR9fUPhQ



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
