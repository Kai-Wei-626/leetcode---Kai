'''
动态规划算法的典型四个步骤如下：

先从实际例子中观察nums的最大子序列的特征。举例子：nums[0], nums[0:2], nums[0:3] ......（如下图）
然后可归纳出一个递推表达式。（如下图）
最后求解。书写代码如下。
构造解。这道题没要求输出子序列，可省去。
再说点废话：

动态规划算法的核心就是递推关系的构造了。
难想到的就是需要把每步的最小值记录，但通过归纳总结也能看出来。

'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minToCur = [0 for i in range(len(nums))]
        maxToCur = [0 for i in range(len(nums))]
        product = [0 for i in range(len(nums))]
        minToCur[0] = nums[0]
        maxToCur[0] = nums[0]
        
        #print(minToCur, maxToCur)
        for i in range(1, len(nums)):
            
            #print(nums[i],minToCur, maxToCur)
            minToCur[i] = min(minToCur[i-1] * nums[i], maxToCur[i-1] * nums[i], nums[i])
            maxToCur[i] = max(minToCur[i-1] * nums[i], maxToCur[i-1] * nums[i], nums[i])

    
        return max(maxToCur)                    
        

        
