# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if head == None or k == 0 or head.next == None:
            return head

        dummy_node = ListNode(-1)
        dummy_node.next = head
        new_head = dummy_node.next
        next_node = dummy_node.next

        # find the length of the list
        len = 1
        while next_node.next != None:
            len += 1
            next_node = next_node.next

        # find the pos
        pos = k % len
        if pos == 0:
            return head

        # find the new head
        while len-pos > 1:
            new_head = new_head.next
            pos += 1
        
        result = new_head.next
        new_head.next = None

        # connect old tail with old head
        next_node.next = dummy_node.next
        return result

if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    sol.rotateRight(node1,1)

