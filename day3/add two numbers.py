'''
1. 要create dummy head， 为了能够生成新的linked list
2. 要tail = dummy， 为了保持dummy作为head node
3. 两个lists长度不等时， 把none type 的node的value = 0， 方便相加
4. 
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        Dummy = ListNode(None)
        tail = Dummy
        while l1 or l2 or add:
            p = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            if p >= 10:
                add = 1
            else: 
                add = 0
            Quotient = p//10
            Remainder = p%10
            tail.next = ListNode(Remainder)
            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return Dummy.next
