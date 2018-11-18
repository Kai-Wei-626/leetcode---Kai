
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cur = []
        res = []
        k = 0
        self.helper(s, cur, res, k)
        return res
        
    def helper(self, s, cur, res, k):
        #dfs stop rule: because ip address can only have 4 sections, so that if it exceeds 4 section, the dfs return
        if k > 4:
            return
        #dfs meet requirement rule
        if s == '' and len(cur) == 4:
            res.append(str('.'.join(cur)))
            return
        # every time we pick fisrt i element of the string
        for i in range(1, 4):
            if i > len(s):
                break
            if self.isValid(s[:i]):
                cur.append(s[:i])
                self.helper(s[i:], cur, res, k+1)
                cur.pop()
          
    def isValid(self, string):
        if len(string) > 1 and string[0] == '0':
            return False
        return int(string) >= 0 and int(string) <= 255
