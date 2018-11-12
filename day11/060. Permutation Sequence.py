'''
My solution exceeds time limit
'''
#exceed time limitation
class Solution:
    def __init__(self):
        self.count = 0
        self.result = []

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n+1)]
        curr =[]
        #count = 0
        result = []
        self.helper(nums, [False] * n, curr, k)
        return ''.join(self.result)
        
        
    def helper(self, nums, used, curr, k):
        #print(self.count, self.result)
        if self.result != []:
            return
        if len(nums) == len(curr):
            self.count += 1
            if self.count == k:   
                self.result = list(curr)
                #print(self.count, self.result)
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            else:
                curr.append(str(nums[i]))
                used[i] = True
                self.helper(nums, used, curr, k)
                used[i] = False
                curr.pop()
