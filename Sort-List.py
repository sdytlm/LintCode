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
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if head == None or head.next == None:
            return head

        # Find the pivot
        dummy_node = ListNode(0,None)
        dummy_node.next = head
        pivot = dummy_node
        fast_node = dummy_node

        while fast_node != None and fast_node.next != None:
            fast_node = fast_node.next.next
            pivot = pivot.next

        pivot.next = None
        l1 = head
        l2 = pivot.next
        # This is for l1. Make sure l1 is terminated
        pivot.next = None

        return self.mergeTwoLists(self.sortList(l1),self.sortList(l2))


    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        if l1 == None and l2 != None:
            return l2
        if l1 != None and l2 == None:
            return l1

        # Dummy Node
        result = ListNode(-1,None)
        head = result

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        # l1 or l2 is not done
        while l1 != None:
            head.next = l1
            l1 = l1.next
            head = head.next
        while l2 != None:
            head.next = l2
            l2 = l2.next
            head = head.next

        return result.next

   
