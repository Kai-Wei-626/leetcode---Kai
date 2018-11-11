'''
hard to find where to start
but since we can't just use x**y, so I guess using recursion is resolution that firstly comes into mind
'''

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #recursion problem
        # n can be odd or even
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        
        if n%2==1:
            return x*self.myPow(x**2, n//2)
        else:
            return self.myPow(x**2, n//2)
        
        
    
        
        
