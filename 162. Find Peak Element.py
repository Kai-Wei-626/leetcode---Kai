class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # compare the mid element with last elemnet
        # if mid > last, go to left
        # if mid <= last, go to right
        if len(nums) == 0:
            return None
        
        leftNum = [float('-inf')]
        rightNum = [float('-inf')]
        leftNum.extend(nums)
        leftNum.extend(rightNum)
        nums = leftNum
        
        left = 1
        right = len(nums) - 2
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1
            
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
            
        
                
        
        
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # compare the mid element with last elemnet
        # if mid > last, go to left
        # if mid <= last, go to right
        if len(nums) == 0:
            return None

        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right)//2
            
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
            
        return left
                
        
        
        
