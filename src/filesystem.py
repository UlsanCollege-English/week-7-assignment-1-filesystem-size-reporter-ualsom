class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []

def total_size(node):
    # TODO: postorder sum
    pass

def folder_sizes(root):
    # TODO: return dict {folder_name: total_bytes}
    pass

def level_order(root):
    # TODO: BFS levels, return list of lists of names
    pass
