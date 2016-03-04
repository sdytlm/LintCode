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
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """ 
    def findNode(self, root, value):
        if root == None:
            return None

        if root.val == value:
            return root
        if root.val > value:
            return self.findNode(root.left, value)
        else:
            return self.findNode(root.right, value)
        
    def deleteNoLeftNode(self, root,node):
        if root.left == node:
            root.left = node.right
            return
        if root.right == node:
            root.right = node.right
            return

        if root.val > node.val:
            self.deleteNoLeftNode(root.left,node)
        else:
            self.deleteNoLeftNode(root.right,node)
        return

    def findLargestChild(self,node):
        while node.left != None:
            node = node.left
        while node.right != None:
            node = node.right
        return node

    def replaceNode(self,root, newNode, oldNode):
        if root.left == oldNode:
            root.left = newNode
            return
        if root.right == oldNode:
            root.right = newNode
            return
        if root.val > oldNode.val:
            self.replaceNode(root.left,newNode, oldNode)
        else:
            self.replaceNode(root.right,newNode,oldNode)
        return

    def removeNode(self, root, value):
        # write your code here
        if root == None:
            return None
        # find the target
        node = self.findNode(root,value)
        if node == None:
            return root
        
        # no left child, just delete or replace by the right child
        if node.left == None:
            if root.val == value:
                return None
            self.deleteNoLeftNode(root,node)
            return root
        # has left child, need to find the most right one to replace
        LargestChild = self.findLargestChild(node)
        # delete largestchild
        self.deleteNoLeftNode(root,LargestChild)
        LargestChild.left = node.left
        LargestChild.right = node.right
        # replace node with largestchild
        if root.val == value:
            return LargestChild

        self.replaceNode(root,LargestChild,node)

        return root
