'''
陷入了一个思维误区， 当时在想在那里添加这条代码，
if i>0 and nums[i] == nums[i-1] and used[i-1]:
以为答案是由重复序列中的第一个数字所产生的递归中产生的， 而实际上答案是由最后一个在重复数字中产生的递归序列所生成的
不过如果代码改成
if i< len(nums)-1 and nums[i] == nums[i+1] and used[i+1]:
递归的产生顺序则相反

首先来看permutation I 的输出顺序
       1                  1                     2
[1,1,2],[1,2,1]     [1,1,2],[1,2,1]       [2,1,1], [2,1,1]

after added this logic  if i>0 and nums[i] == nums[i-1] and used[i-1]:
输出顺序改变:
[]     ,[]          [1,1,2], [1,2,1]         []   ,[2,1,1]  

永远是从最后一个重复的数字那里开始真正的递归。

'''


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr = []
        result = []
        used = [False] * len(nums)
        
        self.helper(sorted(nums), used, curr, result)
        #result = self.dedup(result)
        return result
        
    def helper(self, nums, used, curr, result):
        if len(curr) == len(used):
            result.append(list(curr))
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i] == nums[i-1] and used[i-1]: # where dudup happens
                continue
            else:
                curr.append(nums[i])
                used[i] = True
                self.helper(nums, used, curr, result)
                curr.pop()
                used[i] = False
