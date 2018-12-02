'''
3 steps:
1. use slow and fast node to find the middle node
2. reverse the right half list
3. link them together
'''

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return 
        
        #find the middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half list
        rightHead = slow.next
        slow.next = None
        rightHead = self.reverseList(rightHead)
        #cut the list in the 2 lists
        
        leftHead = head
        while rightHead:
            Next = leftHead.next
            leftHead.next = rightHead
            rightHead = rightHead.next
            leftHead = leftHead.next
            leftHead.next = Next
            leftHead = leftHead.next


    def reverseList(self, head):
        m_pre = ListNode(0)
        m_pre.next = head
        m_post = head.next
            
        while head.next:
            head.next = m_post.next
            m_post.next = m_pre.next
            m_pre.next = m_post
            m_post = head.next
        
        return m_pre.next
