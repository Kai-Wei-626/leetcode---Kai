# normal algo
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            rem = n % 2
            n = n // 2
            res += rem
        return res

# bitwise opreation
'''
why 11 & 7 = 3?

Because if we translate 11 to bit number, 11 = 1011 and 7 is 0111, 
in these 2 numbers, if bitwisely both digits are 1, then return 1; if both digits are 0, return 0; if one of them is 1 and 
the other is 0, return 0
'''
class Solution(object):
    def hammingWeight(self, n):

        bits = 0;
        mask = 1;
        for i in range(32):
            if (n & mask) != 0 :
                bits += 1
                print('i= ',i, n, mask)
            
            mask <<= 1;
        
        return bits;

