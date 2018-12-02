'''
https://www.jianshu.com/p/1c59b153308c
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                first = fast
        
                while head != first:
                    head = head.next
                    first = first.next
                return first
        
        return None
        
