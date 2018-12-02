##cnm, exceed time limit? T T

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        boolean = [False]

        self.helper(s, wordDict, boolean)

        return boolean[0]

    def helper(self, s, wordDict, boolean):
        if s == "":
            boolean[0] = True
            return
            
        for w in wordDict:
            l = len(w)
            if l > len(s):
                continue
            if s[0:l] == w:
                self.helper(s[l:], wordDict, boolean)
                if boolean[0] == True:
                    return

                
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        maps = {}
        return self.helper(s, maps, set(wordDict))

    def helper(self, s, maps, wordDict):
        print(s, maps)
        if s in maps: return maps[s]
        if s in wordDict:
            maps[s] = True
            return True

        for i in range(1, len(s)):
            r = s[i:]
            if r in wordDict and self.helper(s[0:i], maps, wordDict):
                maps[s] = True
                return True

        maps[s] = False
        return False
