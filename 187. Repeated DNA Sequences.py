class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        res = []
        for i in range(len(s) - 10 + 1):
            try:
                if d[s[i:i+10]] == 1:
                    res.append(s[i:i+10])
                d[s[i:i+10]] += 1
            except:
                d[s[i:i+10]] = 1
        
        
        return res
    
