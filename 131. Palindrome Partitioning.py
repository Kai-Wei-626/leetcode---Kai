'''
For loop + BackTracking.
'''
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        cur = []
        res = []
        self.helper(s, cur, res)
        return res
    
    def helper(self, s, cur, res):
        if s == '':
            res.append(list(cur))
            return
        
        for i in range(1, len(s)+1):
            if not self.isP(s[:i]):
                continue
            else:
                cur.append(s[:i])
                self.helper(s[i:], cur, res)
                cur.pop()
                
    def isP(self,s ):
        if s == s[::-1]:
            return True
        else:
            return False
