# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        extra = ListNode(0) # dummy head for elements less than x
        extra1 = extra #moving pointer for elements less than x
        
        #first is iterator
        while first.next:
            if first.next.val < x:
                extra1.next = first.next
                extra1 = extra1.next
                #extra1.next = None
                # jump over the first.next
                first.next = first.next.next
            
            #no matter what, first advances to next node
            else:
                first = first.next
            
        extra1.next = dummy.next
        return extra.next
            
           
            
            
            
            
            
            
