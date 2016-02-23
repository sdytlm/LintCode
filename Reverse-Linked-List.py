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
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if head == None or head.next == None:
            return head

        Dummy_node = ListNode(-1,None)
        Dummy_node.next = head
        front_node = Dummy_node.next
        end_node = front_node.next

        
        while end_node != None:
            next_node = end_node.next
            end_node.next = front_node
            front_node = end_node
            end_node = next_node

        head.next = None
        return front_node
