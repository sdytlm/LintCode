"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def builder(self, preorder,preorder_left,preorder_right,inorder,inorder_left,inorder_right,hash_map):
        if preorder_left > preorder_right or inorder_left > inorder_right:
            return None
        # preorder_left point to the root
        root = TreeNode(preorder[preorder_left])
        
        # Get the index of root in inorder list
        inorder_index = hash_map[root.val]

        # split the inorder list
        # inorder_index-inorder_left == num of nodes in left tree
        root.left = self.builder(preorder,preorder_left+1,preorder_left+(inorder_index-inorder_left),inorder,inorder_left,inorder_index-1,hash_map)
        root.right = self.builder(preorder,preorder_left+1+(inorder_index-inorder_left),preorder_right,inorder,inorder_index+1,inorder_right,hash_map)
        
        return root
        
    
    def buildTree(self, preorder, inorder):
        # write your code here
        # build a hash map <inorder[i], i>
        if len(preorder)==0 or len(inorder)==0 or len(preorder)!=len(inorder):
            return None
        hash_map = dict()
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i

        return self.builder(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,hash_map)

