'''
just 2 loops
Using GREEDY
'''

class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ret = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i+1] > ratings[i]:
                ret[i+1] = ret[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i-1] > ratings[i]:
                if ret[i-1] < ret[i]+1:  #make sure won't replace with lower value
                    ret[i-1] = ret[i] + 1 
        return sum(ret)
                
