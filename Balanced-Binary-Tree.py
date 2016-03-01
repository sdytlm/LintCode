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
    @return: True if this Binary tree is Balanced, or false.
    """
    def maxPath(self, root):
        if root.left!=None:
            left = self.maxPath(root.left)
        else:
            left = 0
        if root.right!=None:
            right = self.maxPath(root.right)
        else:
            right = 0

        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        else:
            return max(left,right)+1

    def isBalanced(self, root):
        # write your code here
        if root == None:
            return True
        if self.maxPath(root) == -1:
            return False
        else:
            return True
