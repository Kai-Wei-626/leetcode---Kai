class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        
        if l2 == 0:
            return 0
        for i in range(len(haystack)):
            if i + l2 <= l1 and haystack[i:i+l2] == needle:
                    return i
            else:
                continue
        return -1
