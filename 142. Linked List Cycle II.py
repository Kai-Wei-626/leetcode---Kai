'''
https://www.jianshu.com/p/1c59b153308c

   a    b
1 -- 2 -- 3
       e / \  c
        5 -- 4         
          d
digits represent the node, and letters represent the distance

if slow pointer and fast pointer start at node 1, they will meet in node 4. 
In thie process, fast pointer always goes twice as far as the slow pointer.
so we have: L(fast) = 2*L(slow),

2(a+b+c) = a+b+c+d+e+c  
=> a+b = d+e
from the chart above, we can tell from 4 to 3, it takes d+e to get to 3, which is the node where cycle begins. in
the meantime, the head node take a+b to get to the node 3. Therefore, we have

1.next.next = 3  
4.next.next = 3
the node they meet is the node where the cycle begins          
         
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
        
