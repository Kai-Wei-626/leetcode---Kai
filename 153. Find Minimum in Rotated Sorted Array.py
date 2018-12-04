class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        
        while left <= right:
            mid = (left + right)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[-1]:
                left = mid+1
            else:
                right = mid-1
        
