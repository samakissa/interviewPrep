# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPreOrder(root):

    if root:
        print(root.val)
        printPreOrder(root.left)
        printPreOrder(root.right)

graph = Node(1)
graph.left = Node(2)
graph.right = Node(3)
graph.left.left = Node(3)
graph.left.right = Node(5)

printPreOrder(graph)
