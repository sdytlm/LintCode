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
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        # split the list from the middle
        # reverse the right sublist
        # merge the two lists

        if head==None or head.next==None:
            return head

        # find the pivot
        dummy = ListNode(0,None)
        fast_node = dummy
        pivot = dummy
        dummy.next = head

        while fast_node != None and fast_node.next != None:
            fast_node = fast_node.next.next
            pivot = pivot.next
        
        right_list = pivot.next
        # terminate the left list
        pivot.next = None
        left_list = head

        # reverse the right list
        prev_node = right_list
        next_node = right_list.next
        # terminate the right list
        prev_node.next = None

        while next_node != None:
            tmp_point = next_node.next
            next_node.next = prev_node
            prev_node = next_node
            next_node = tmp_point
        
        right_list = prev_node
        
        # merge right_list and left_list
        dummy.next = left_list
        while left_list != None and right_list != None:
            next_left = left_list.next
            left_list.next = right_list
            next_right = right_list.next
            right_list.next = next_left
            left_list = next_left
            right_list = next_right
        
        return dummy.next
