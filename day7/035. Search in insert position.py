'''
这道题 edge case 过于复杂。 不知道有没有更general，simple一点的算法
连续了fail了三次edge case。。。
‘’‘
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > target:
                #mid = mid -1
                right = mid
            elif nums[mid] < target:
                mid = mid + 1
                left = mid
            else:
                return mid
        if target > nums[mid]:
            mid = mid + 1
        return mid

                
