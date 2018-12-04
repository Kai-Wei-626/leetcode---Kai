#beat 99.5%
        
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        l = s.split()
        for i in reversed(range(len(l))):
            res.append(l[i])
        
        return ' '.join(res)
            
