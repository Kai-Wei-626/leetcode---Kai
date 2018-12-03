#merge sort
#time complexity: O(nlogn)   space complexity(O(logn))
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while (l1 and l2):
            if (l1.val > l2.val):
                temp  = l1
                l1 = l2
                l2 = temp
            tail.next = l1
            l1 = l1.next
            tail = tail.next

        if l1: tail.next = l1
        if l2: tail.next = l2
        return dummy.next
