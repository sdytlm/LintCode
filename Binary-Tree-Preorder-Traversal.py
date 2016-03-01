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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorder(self, node, result):
        result.append(node.val)
        if node.left != None:
            self.preorder(node.left,result)
        if node.right != None:
            self.preorder(node.right,result)
        return result

    def preorderTraversal(self, root):
        # write your code here
        result = []
        if root == None:
            return result
        self.preorder(root,result)
        return result
