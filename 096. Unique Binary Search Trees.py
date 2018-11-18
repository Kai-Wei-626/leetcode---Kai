#就是找规律， 然后注意不要edge case， case out of index 之类的问题

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                #print(i,j,i-j-1)
                #print('aaa ',dp[0], dp[1], dp[2])
                dp[i] += dp[j] * dp[i - j - 1]
        
        return dp[n]
