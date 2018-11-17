class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp = [0]*len(s)
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        
        w1 = 1
        w2 = 1
        
           
        for i in range(1, len(s)):
            w = 0
            if not self.isValid1(s[i]) and not self.isValid2(s[i-1], s[i]):
                return 0
            if self.isValid1(s[i]):
                w = w1
            if self.isValid2(s[i-1], s[i]):
                w += w2
            w2 = w1
            w1 = w
            
        return w1
    
    def isValid1(self, string):
        if string == '0':
            return False
        else:
            return True
    def isValid2(self, string1, string2):
        if 10 <= int(string1+ string2) <= 26:
            return True
        else:
            return False
        
        
