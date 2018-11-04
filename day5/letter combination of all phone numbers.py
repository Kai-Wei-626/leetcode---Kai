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
