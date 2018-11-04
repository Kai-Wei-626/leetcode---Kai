'''
roman to int
'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i,c in enumerate(s):
            next_char = s[i+1] if i+1 < len(s) else 'nothing'
            
            if c == 'M':
                ret = ret + 1000
            if c == 'D':
                ret = ret + 500
            if c == 'C':
                ret += 100 if next_char not in 'DM' else -100
            if c == 'L':
                ret += 50
            if c == 'X':
                ret += 10 if next_char not in 'LC' else -10
            if c == 'V':
                ret += 5
            if c == 'I':
                ret += 1 if next_char not in 'XV' else -1
        return ret
