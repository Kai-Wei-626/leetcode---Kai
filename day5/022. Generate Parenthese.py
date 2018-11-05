class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        def backTracking(s = '', left=0, right=0):
            if len(s) == 2 * n:
                ret.append(s)
                return 
            if left < n:
                backTracking(s+'(', left+1, right)
            if right < left:
                backTracking(s+')', left, right + 1)
                
        backTracking()
        return ret
            
        
