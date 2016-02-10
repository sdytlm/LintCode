"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
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
