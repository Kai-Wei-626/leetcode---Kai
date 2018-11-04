'''
from
https://github.com/criszhou/LeetCode-Python/blob/master/017.%20Letter%20Combinations%20of%20a%20Phone%20Number.py
'''
class Solution(object):
    buttonToLetters = { str(i):s for i,s in enumerate([" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]) }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        ret = ['']
        for c in digits:
            #print(c)
            #print(self.buttonToLetters[c])
            ret = [a+b for a in ret for b in self.buttonToLetters[c] ]
        return ret

    
    
#
'''
https://buptwc.github.io/2018/10/31/Leetcode-17-Letter-Combinations-of-a-Phone-Number/
'''
class Solution(object):
    buttonToLetters = { str(i):s for i,s in enumerate([" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]) }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = ['']
        temp = []
        for i in digits:
            print(i)
            for s in ret:
                print('as ',s)
                for s_plus in self.buttonToLetters[i]:
                    temp.append(s+s_plus)
            
            ret = temp
            temp = []
        return ret
                         
