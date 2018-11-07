'''
http://bangbingsyb.blogspot.com/2014/11/leetcode-search-in-rotated-sorted-array.html
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid 
            if nums[end] < nums[mid]: # left array sorted
                if nums[start] <= target and target < nums[mid]: # in the if statement, don't forget use <=
                    mid -= 1
                    end = mid
                else:
                    mid += 1
                    start = mid
            
            else:   # right half array sorted
                if nums[end] >= target and target > nums[mid]:
                    mid += 1
                    start = mid
                else:
                    mid -= 1
                    end = mid
        return -1
            
