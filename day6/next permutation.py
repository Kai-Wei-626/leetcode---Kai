class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 
        replace = len(nums) - 2
        while replace >= 0:
            if nums[replace] > nums[replace+1]:
                replace -= 1
            else:
                break
        if replace < 0:
            nums = sorted(nums)

        else:
            lgindex = replace + 1
            while lgindex < len(nums) and nums[lgindex] > nums[replace]:
                lgindex += 1
            nums[replace], nums[lgindex-1] =  nums[lgindex-1],nums[replace]
            nums[replace+1: len(nums)] = sorted(nums[replace+1: len(nums)])
        
