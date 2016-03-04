"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            return node
        if root.val > node.val:
            if root.left == None:
                root.left = node
            else:
                self.insertNode(root.left,node)
        else:
            if root.right == None:
                root.right = node
            else:
                self.insertNode(root.right,node)
        return root
