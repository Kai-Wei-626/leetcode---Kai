class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        cur = []
        res = []
        s = 0
        candidate = [i+1 for i in range(n)]
        self.helper(candidate, k, s, cur, res)
        return res
    def helper(self, candidate, k, s, cur, res):
        if len(cur) == k:
            res.append(list(cur))
            return
        for i in range(s, len(candidate)): ## won't out of index as range(n,n) returns nothing
            cur.append(candidate[i])
            self.helper(candidate, k, i+1, cur, res)
            cur.pop()
