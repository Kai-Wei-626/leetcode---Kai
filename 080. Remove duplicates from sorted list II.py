class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        
        s = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[s] or nums[i] != nums[s-1]: # this if condition assure 2 duplicates
                s = s+1
                nums[s] = nums[i]
            else:
                continue
                
        return s+1
            
            
