"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize_helper(self, root, ret):
        ret.append(root.val)
        if root.left != None:
            self.serialize_helper(root.left, ret)
        else:
            ret.append('#')
        if root.right != None:
            self.serialize_helper(root.right,ret)
        else:
            ret.append('#')
        return ret

    def serialize(self, root):
        # write your code here
        ret = []
        if root == None:
            return ret
        self.serialize_helper(root,ret)
        return ret

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given 
    by system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize_helper(self, data):
        if data == None:
            return None
        if data[0] == '#':
            data.pop(0)
            return None

        Node = TreeNode(data[0])
        data.pop(0)
        Node.left = self.deserialize_helper(data)
        Node.right = self.deserialize_helper(data)
        return Node

    def deserialize(self, data):
        # write your code here
        if data == None or len(data) == 0:
            return None
        return self.deserialize_helper(data)

