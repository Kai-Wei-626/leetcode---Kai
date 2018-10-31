'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
# 2 pointer

class Solution(object):
    def removeDuplicates(self, nums):
        #pointer1=0 #constantly moving 
        pointer2=0 #moving when the next one is not equal to the cur one
        if nums == []:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] != nums[pointer2]:

                    pointer2 += 1
                    nums[i], nums[pointer2] = nums[pointer2], nums[i]
            return pointer2 + 1
