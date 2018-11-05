# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        first = dummy
        while l1 and l2:
            if l1.val > l2.val:
                first.next = l2
                first = first.next
                l2 = l2.next
            else:
                first.next = l1
                first = first.next
                l1 = l1.next
        ############################Don't forget the below part######################
        if l1 == None:
            first.next = l2
        if l2 == None:
            first.next = l1
        return dummy.next
