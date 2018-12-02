'''
totally did by myself without reference!!!
'''

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
       
        post = head.next
        

        while post:
            # if post val is larger and equal than head val, both move on to next
            if post.val >= head.val:
                head = head.next
                post = post.next
            # if post val less than, start insert. make sure set pre = dummy at the end once insert happened
            else:
                if pre.next.val >= post.val:
                    head.next = post.next
                    post.next = pre.next
                    pre.next = post
                    post = head.next
                    pre = dummy
                else:
                    pre = pre.next
        
        return dummy.next
