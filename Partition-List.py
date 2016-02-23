"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head == None or head.next == None:
            return head

        dummy = ListNode(0,None)
        left_list = dummy
        dummy2 = ListNode(0,None)
        right_list = dummy2

        while head != None:
            if head.val < x:
                left_list.next = head
                left_list = left_list.next
            else:
                right_list.next = head
                right_list = right_list.next
            head = head.next
        # connect left_list and right_list
        left_list.next = dummy2.next
        # terminate the right list
        right_list.next = None
        return dummy.next
