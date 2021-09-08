class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, low, high):

    sumBST = 0

    def PreOrderTraversal(root: TreeNode,low, high):
        if root and root.val != None:
            nonlocal sumBST
            if low <= root.val <= high:
               sumBST  += root.val
            PreOrderTraversal(root.left,low, high)
            PreOrderTraversal(root.right,low, high)
    PreOrderTraversal(root,low, high)
    print(sumBST)
    return sumBST

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(None)
root.right.right = TreeNode(18)

rangeSumBST(root,7,15)
