'''
3 stupid edge cases, this can't be the best.
'''

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 2:
            return 1
        if x == 0:
            return 0

        left = 0
        right = x
        while left < right:
            mid = (left + right)//2
            
            if x >= (mid-1)**2 and x < mid ** 2:
                return mid-1
            elif x >= mid**2:
                left = mid
            else:
                right = mid


#clean and neat
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 1
        right = x
        while left <= right:
            mid = (left + right)//2
            
            if x == mid ** 2:
                return mid
            elif x >= mid**2:
                left = mid + 1
            else:
                right = mid - 1
                
        return left - 1

