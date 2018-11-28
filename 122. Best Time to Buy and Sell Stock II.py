class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        left = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                continue
            else:
                profit += prices[i-1] - prices[left]
                left = i
        profit += prices[i] - prices[left]
        return profit
                
                
                
