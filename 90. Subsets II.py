# im surprised this solution does not exceed time limit
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        cur = []
        s = 0
        for i in range(len(nums)+1):
            self.helper(nums, s, i, cur, res)
        return res
    
    def helper(self, nums, s, k, cur, res):
        if len(cur) == k and cur not in res: # how to optimize this logic? other ways to check the duplicates?
            res.append(list(cur))
            return
        
        for i in range(s, len(nums)):
            
            cur.append(nums[i])
            self.helper(nums, i+1, k, cur, res)
            cur.pop()
            
