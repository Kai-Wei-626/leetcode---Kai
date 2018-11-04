'''
time out O(nlogn) + O(n^2) solution.  
firstly, sort
secondly, fix one pointer, then see the rest as a 2 sum case
'''

## 3 sum        
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        #print(nums)
        rel = []
        for i in range(len(nums)-1):
            left = i+1 
            right = len(nums) - 1
            #print(i,left,right)
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    rel.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
        rel1 = []
        for i in range(len(rel)):
            if rel[i] not in rel1:
                rel1.append(rel[i])
            
        return rel1
