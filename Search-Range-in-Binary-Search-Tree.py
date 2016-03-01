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
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """ 
    def searchRange(self, root, k1, k2):
        # write your code here
        result = []
        if root == None:
            return result
    
        if root.left != None:
            left_result = self.searchRange(root.left,k1,k2)
        else:
            left_result = []

        result = result + left_result

        if root.val>=k1 and root.val <=k2:
            result.append(root.val)

        if root.right != None:
            right_result = self.searchRange(root.right,k1,k2)
        else:
            right_result = []

        result = result + right_result

        return result
