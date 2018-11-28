class Solution:
    def maxProfit(self, prices):
        length=len(prices)
        if length==0: return 0
        f1=[0 for i in range(length)]
        f2=[0 for i in range(length)]
        
        minV = prices[0]
        for i in range(1, length):
            minV = min(minV, prices[i]) # the minimal value in the positions before i 
            f1[i] = max(f1[i-1], prices[i] - minV) # the maximum profit before i    
        
        maxV = prices[length - 1]
        for i in range(length-2, -1, -1):
            maxV = max(maxV, prices[i]) # the maximum value in the positions after i
            f2[i] = max(f2[i+1], maxV - prices[i]) # maximum profit after day i
        
        res = 0
        for i in range(length):
            if f1[i] + f2[i] > res:
                res = f1[i] + f2[i]
       
        return res
            
