# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        # Deep copy: coppy the whole list and connect all node together
        if head == None:
            return head
        # hash_map: {node_in_old_list, node_in_new_lsit}
        hash_map = {}
        dummy = RandomListNode(0)
        cur = dummy

        while head != None:
            # check if head in the hash_map
            if hash_map.has_key(head):
                new_node = hash_map[head]
            else:
                # create new one
                new_node = RandomListNode(head.label)
                hash_map[head] = new_node
           
            # new_node.next will be connected by the following line.
            cur.next = new_node
            
            # need to fix the new_node.random
            if head.random != None:
                if hash_map.has_key(head.random):
                    new_node.random = hash_map[head.random]
                else:
                    new_random_node = RandomListNode(head.random.label)
                    new_node.random = new_random_node
                    hash_map[head.random] = new_random_node
            cur = cur.next
            head = head.next
        return dummy.next
