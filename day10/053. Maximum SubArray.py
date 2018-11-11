'''
这道题的重点在于如何比较，比较哪些数
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = nums[0]
        maxMaxSum = maxSum
        if len(nums) == 1:
            return maxSum
        
        for i in range(1, len(nums)):
            maxSum = max(nums[i], nums[i] + maxSum)
            maxMaxSum = max(maxSum, maxMaxSum)
        return maxMaxSum    
  
  
  
#solution 2
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1, len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
        return max(nums)
        
