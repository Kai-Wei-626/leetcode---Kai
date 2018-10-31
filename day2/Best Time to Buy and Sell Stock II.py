"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
"""

def maxProfit(prices):
    pointer = 0
    sum1 = 0
    for i in range(len(prices)-1):
        if prices[i+1] >= prices[i]:
            sum1 += price[i+1] - price[i]
        
