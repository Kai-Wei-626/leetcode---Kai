'''
1. My solution  1 exceeds time limit
2. solution 2 is using some tricks with factorial(n)
    if n = 3, then it can be takes apart by
        1 [2, 3]
        1 [3, 2]
        2 [1, 3]
        2 [3, 1]
        3 [1, 2]
        3 [2, 1]
   so the list comes in order, then the number of all the list is n * factorial(n-1)
   so k%factorial(n-1) is the first digit of the return list.
'''
#using backtracking exceeds time limitation
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
                

##using tricks explained in the beginning      
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i for i in range(1, n+1)]

        fact = [0] * n
        fact[0] = 1
        for i in range(1, n):
            fact[i] = i * fact[i - 1]

        k = k - 1
        index = 0
        sb = []
        for i in reversed(range(n)):
            index = k//fact[i]  ## 3//2 = 1
            k = k%fact[i]  ##  3%2 = 1
            sb.append(str(nums[index]))
            del nums[index]


        return ''.join(sb)
