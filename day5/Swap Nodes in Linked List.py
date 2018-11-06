class ListNode()
    def __init__(self, n):
      self.val = n
      self.next = None
    
    
class Solution()
    def swapPairs(self, head):
        dummy = ListNode(0):
        first = dummy
        dummy.next  = head

        while first.next and first.next.next:
            next1 = first.next
            next2 = first.next.next
            next3 = first.next.next.next

            first.next = next2
            next2.next = next1
            next1.next = next3

            first = next1

        return dummy.next

  
  
