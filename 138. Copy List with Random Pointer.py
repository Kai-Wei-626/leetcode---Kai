'''
deepcopy means that we have create a new node with copied node's value
several points to keep in mind:
1. map store the original node as the key, and the newly copied node as the value
2.

'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        cur = dummy
        maps = {}

        while head:
            ## copy the current node if necessary
            if head not in maps.keys():
                maps[head] = RandomListNode(head.label)

            ## connext the copied node to the deep copy list
            cur.next = maps[head]

            ## copy the random node if necessary.
            if head.random:
                if head.random not in maps.keys():
                    maps[head.random] = RandomListNode(head.random.label)
                ## connect the copied node to the random pointer
                cur.next.random = maps[head.random]

            head = head.next
            cur = cur.next

        return dummy.next

## solution 2    
class Solution(object):
    def copyRandomList(self, head):
        #first loop: insertion
        cur = head
        while cur:
            #make a copy of cur node, insert it to the middle of cur and cur.next
            copy = RandomListNode(cur.label)
            copy.next = cur.next
            cur.next = copy
            cur = cur.next.next

        # Second loop, link the random pointer
        cur = head # reset cur
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # third pass, extracted copioed node
        cur = head  
        dummy = RandomListNode(0)
        copyhead = dummy
        while cur:
            copyhead.next = cur.next
            cur.next = cur.next.next # jump over the original node
            copyhead = copyhead.next
            cur = cur.next

        return dummy.next
