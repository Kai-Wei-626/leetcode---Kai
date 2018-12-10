class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = ''
        while n != 0:
            rem = n % 2 
            n = n // 2
            s = str(rem) + s
        
        for i in range(32 - len(s)):
            s = '0' + s
        
        # reverse string
        s = s[::-1]
        
        power = 0
        res = 0
        for i in reversed(range(len(s))):
            res = res + int(s[i]) * (2**power)
            power += 1
            
        
        return res  
    
