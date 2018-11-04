class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #2n -1 center point in a string
        if len(s) == 0:
            return ''
        maxlen = 0
        start = 0
        end = 0
        for i in range(len(s) - 1):
            len1 = self.expand(s,i,i)
            len2 = self.expand(s,i, i+1)
            #print(i)
            #print('length ',len1,len2)
            maxlen = max(len1, len2)
            if maxlen > (end-start):
                start = i - (maxlen-1)//2
                end = i + maxlen//2
                print('start', start, end)
        return s[start:end+1]   
    
    def expand(self, s, left, right):
        # s[left] == s[right] condition must be put in the end, otherwise will have out of index error
        while  left>=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

    
s = Solution()
s.longestPalindrome('abcbd')  
