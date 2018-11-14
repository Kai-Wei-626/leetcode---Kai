class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cur = []
        res = []
        s = 0
        nums = sorted(nums)
        
        for k in range(len(nums) + 1):
            self.helper(nums, k, s, cur, res)
        
        return res
    
    def helper(self, nums, k, s, cur, res):
        
        if len(cur) == k:
            res.append(list(cur))
            return

        for i in range(s, len(nums)):
            cur.append(nums[i])
            self.helper(nums, k, i+1, cur, res)
            cur.pop()
            
            
            
