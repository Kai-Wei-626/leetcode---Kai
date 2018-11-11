'''
算法有点慢,想了半天。。。设置reach这个dynamic的边界有点难想
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        reach = 0
        i = 0
        for i in range(length):
            if i <= reach: #reach is changing
                reach = max(reach, nums[i] + i)
                if reach >= length - 1:
                    return True
        return False
            
