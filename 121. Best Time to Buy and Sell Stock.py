# brute force
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i])
        
        return profit
        
        
 # o(n) solution
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf') 
        maxPrice = 0
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxPrice:
                maxPrice = prices[i] - minPrice
                
        return maxPrice
