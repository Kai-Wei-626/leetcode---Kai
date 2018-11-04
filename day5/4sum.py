'''
beat 1.35% python 3 submiision???? :)
'''



# 4 sum
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        nums = sorted(nums)
        for i in range(0, len(nums)-3):
            tar  = target - nums[i]
            #print('list: ',nums[i+1: len(nums)])
            x = self.threeSum(nums[i+1: len(nums)], tar)
            #print(x)
            if x != []:
                for l in x:
                    l.append(nums[i])
                    ret.append(l)
        ret1 = []
        for i in ret:
            if i not in ret1:
                ret1.append(i)
        return ret1
        
        
    def threeSum(self, nums, target):
        ret = []
        
        for i2 in range(1, len(nums) - 1):
            
            i1 = 0
            i3 = len(nums)-1
            #print(i1,i2,i3)
            while i1<i2<i3:
                #print(" ", i1,i2,i3)
                currSum = nums[i1] + nums[i2] + nums[i3]
                #print("cur: ",currSum)
                if currSum == target:
                    ret.append([nums[i1],nums[i2],nums[i3]])
                    i1 += 1
                    i3 -= 1
                elif currSum > target:
                    i3 -= 1
                else:
                    i1 += 1          
        return ret   
