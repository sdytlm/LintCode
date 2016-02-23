"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""        
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if head == None:
            return None
        if head.next == None:
            new_node = TreeNode(head.val)
            return new_node
        # find middle
        dummy = ListNode(0,None)
        dummy.next = head

        fast_node = dummy
        slow_node = dummy

        while fast_node != None and fast_node.next != None:
            fast_node = fast_node.next.next
            prev_node = slow_node
            slow_node = slow_node.next

        # create the middle node
        middle_node = TreeNode(slow_node.val)
        middle_node.right = self.sortedListToBST(slow_node.next)
        prev_node.next = None
        middle_node.left = self.sortedListToBST(dummy.next)

        return middle_node

