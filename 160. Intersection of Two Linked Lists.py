class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Special cases
        if headA is None or headB is None:
            return 
        
        currA = headA
        currB = headB
        # Get the length of headA and headB
        lenA = 0
        while currA:
            lenA += 1
            currA = currA.next
        
        lenB = 0
        while currB:
            lenB += 1
            currB = currB.next
        
        currA = headA
        currB = headB
        # Cut the longer list
        # to make them with the same length
        if lenB > lenA:
            diff = lenB - lenA
            while diff > 0:
                currB = currB.next
                diff -= 1
                
        if lenA > lenB:
            diff = lenA - lenB
            while diff > 0:
                currA = currA.next
                diff -= 1
        
        # Iterate over the two list to find the intersection
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
