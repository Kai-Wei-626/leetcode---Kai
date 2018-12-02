'''
to avoid none type error, we need to check if fast or fast.next is none
'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next: 
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True
        
