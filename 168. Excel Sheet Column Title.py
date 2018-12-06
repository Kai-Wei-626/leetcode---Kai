class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        s = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        res = ""

        while n > 0:
            q = n % 26
            n = n // 26
            res = s[q] + res
            if q == 0: n -= 1
        return res

