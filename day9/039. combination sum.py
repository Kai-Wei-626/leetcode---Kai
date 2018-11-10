'''
不知道为什么 用 curr.append 和 curr.pop() 的组合最后返回的时空集
？？？
for example, 
ret =[]
cur =[1,2,3]
ret.append(cur)
cur.pop()
??为什么ret 中的list也pop了那

解决方法，
就是把ret.append(cur) 改为 ret.append(list(cur))
'''


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        curr =[]
        result = []
        candidates.sort()
        self.helper(candidates, target,0, curr, result)
        return result
        
        
    def helper(self, remCandidate, remTarget, s, curr, retList):
       # print('round: ',remCandidate, remTarget, s, curr, retList)
        if remTarget == 0:
            retList.append(curr) # retList.append
         #   print('appending: ',remCandidate, remTarget, s, curr, retList)
            return
        
        for i in range(s, len(remCandidate)):
            if remCandidate[i] > remTarget:
                return
            
            #curr.append(remCandidate[i])
            self.helper(remCandidate, remTarget - remCandidate[i], i, curr + [remCandidate[i]], retList)
            #curr.pop()
        
    
