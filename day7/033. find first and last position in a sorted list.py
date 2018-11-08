class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return [self.find_left(0, mid, nums, target), self.find_right(mid,len(nums)-1, nums, target)]
            
        return [-1, -1]
    
    def find_left(self, left, right, nums, target):
        if left == right:  #if input is [1] 1, should return [0,0]
            return right
        
        while left < right:
            if nums[right-1] != target:
                return right
            else:
                right -= 1
        return right
         
    def find_right(self, left, right, nums, target):
        if left == right:
            return left
        while left < right:
            if nums[left+1] != target:
                return left
            else:
                left += 1
        return left
        
