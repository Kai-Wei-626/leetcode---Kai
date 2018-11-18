'''
指针交换位置
m_.next = m_post.next
m_post.next = m_pre.next
m_pre.next = m_post
但要注意m_post位置的变化
所以要再加上一行 m_post = m_.next 来生成新的post node
'''

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        m_pre = dummy
        m_post = dummy.next.next
        m_ = dummy.next
        
        for i in range(m-1):
            m_pre = m_pre.next
            m_post = m_post.next
            m_ = m_.next
        
        
        for i in range(n - m):
            m_.next = m_post.next
            m_post.next = m_pre.next
            m_pre.next = m_post
            
            m_post = m_.next
        
        return dummy.next
            
        
        

        
        
        
        
