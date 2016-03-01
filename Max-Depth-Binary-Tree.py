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
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        if root==None:
            return 0
        if root.left != None:
            left = self.maxDepth(root.left)
        else:
            left = 0
        if root.right != None:
            right = self.maxDepth(root.right)
        else:
            right = 0

        return max(left,right)+1
