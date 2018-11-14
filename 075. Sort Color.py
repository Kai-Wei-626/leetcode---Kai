# simple bubble sort but O(n) = n**2
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # bubble sort
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    

#linear time solution
#make sure use if else statement, not seperate if
# when moving pointer from 1 to n-1, when element == 2, swap them but pointer needs to be pushed back since we
# don't know which element is swapped to the current position.
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
    
        left = 0
        right = len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i = i + 1
            
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
               
            
            else:
                i = i + 1
            
