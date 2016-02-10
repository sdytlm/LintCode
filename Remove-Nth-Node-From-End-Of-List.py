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
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if head == None:
            return None
        length = 1
        tmp = head
        while tmp.next != None:
            length += 1
            tmp = tmp.next
        # corner case: n == length
        if n == length:
            return head.next
        # remove nth lement
        tmp = head
        num = length - n - 1
        while num > 0:
            num -= 1
            tmp = tmp.next
        
        if tmp.next != None:
            tmp.next = (tmp.next).next
        else:
            tmp.next = None
            
        return head
