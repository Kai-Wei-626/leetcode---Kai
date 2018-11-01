'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Rotate to right

example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            self.rotatebyone(nums)
        
    def rotatebyone(self, nums):
        temp = nums[len(nums)-1]
        for i in range(len(nums)-1):
            nums[len(nums)-1-i] = nums[len(nums)-2-i]
        nums[0] = temp
 #time complexity = O(n*k)
 # not optimal
 
 ## solution 2 ( this is actually rotate left)
 def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
 def rotate(arr, d):
    l = len(arr)
    for i in range(gcd(l, d)):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= l:
                k = k - l
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    return(arr)
    
    
