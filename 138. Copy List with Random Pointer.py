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
