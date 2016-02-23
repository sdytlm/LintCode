"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head == None or head.next == None:
            return head
        fast_node = head
        slow_node = head
       
        
        while fast_node != None:
            if fast_node == slow_node:
                fast_node = fast_node.next
            else:
                slow_node.next = fast_node
                slow_node = fast_node
                fast_node = fast_node.next
       # terminate the result
       # 1->2->3->3->None
       slow_node.next = None
       return head
