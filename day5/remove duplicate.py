'''

'''
# when duplicates are rare, use two pointer solution.
# but be careful of edge cases such as ([], 0), or ([1], 1) ----> make sure right = len() not len() -1
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        left = 0
        right = len(nums) 
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
                
        return left
