"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidNode(self,node,upper,lower):
        if node == None:
            return True
        if node.val >= upper or node.val <=lower:
            return False

        if node.left != None and self.isValidNode(node.left,node.val,lower) == False:
            return False
        if node.right != None and self.isValidNode(node.right,upper,node.val) == False:
            return False

        return True
    def isValidBST(self, root):
        # write your code here
        # case: {10,5,15,#,#,6,20} require "upper" and "lower" in recursive
        return self.isValidNode(root,sys.maxint,-sys.maxint-1)
