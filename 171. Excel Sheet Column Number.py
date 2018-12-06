# this one is eaisier than 168
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        d = dict(zip(string.ascii_uppercase, range(1,27)))        
        res = 0    
        for i in range(len(s)):
            res = res*26 + d[s[i]]
        return res
        
        
