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
            
class Solution:
        def reverseWords(self, s):
            return " ".join(s.split()[::-1])

