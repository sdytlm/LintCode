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
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        q = []
        q.append(root)
        result = []
        if root == None:
            return result
    
        while len(q)!=0:
            # size = num of nodes in each level
            size = len(q)
            row = []
            for i in range(size):
                node = q.pop(0)
                row.append(node.val)
                
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            result.append(row)

        return result
