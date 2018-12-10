'''
此题目参考走楼梯的那道题， 相同的dp思路
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # create a list to store the maximum money that robber can get from each house 
		x = [0] * len(nums)
		#edge cases
        if nums == []:
            return 0
        if len(nums) == 1: 
            return nums[0]
        
		# first and second element has to be placed in the beginning to prevent out of index error
        x[0] = nums[0]
        x[1] = max(nums[1], nums[0])
        

        i = 2
        while i <= len(nums) - 1:
			# store the max of (all the money robber get from since beginning to previous house,
			# all the money robber can get since the beginning to the house before plus the current house)
            x[i] = max(x[i-2] + nums[i], x[i-1])
            i += 1
        return x[len(nums) - 1]
