"""Print path with DF treee traversal"""

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# build the tree
leaf1 = Node(1)
leaf2 = Node(4)
leaf3 = Node(6)

branch1 = Node(3, leaf1, leaf2)
root = Node(5, branch1,leaf3)



def print_dfs_paths(curr_node, path=""):
    # base case
    if curr_node.right == None and curr_node.left == None:
        print path + "+" + str(curr_node.data)
        return
    # add to path.  recursive calls.
    path = path + "+" + str(curr_node.data)
    print_dfs_paths(curr_node.left, path)
    print_dfs_paths(curr_node.right, path)



print_dfs_paths(leaf1)
print_dfs_paths(leaf2)
print_dfs_paths(root)


