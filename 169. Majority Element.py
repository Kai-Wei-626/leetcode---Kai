class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        n = len(nums)
        for i in nums:
            d[i] = 0
        
        for i in nums:
            d[i] += 1
            if d[i] > n/2:
                return i
            
