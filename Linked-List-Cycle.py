"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return False

        fast_node = head
        slow_node = head

        while fast_node != None and fast_node.next != None:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            if fast_node == slow_node:
                return True
        return False


