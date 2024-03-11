# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        def dfs(index, cur, total):
            if total == target:
                cur = cur.copy()
                res.append(cur)
                return
            
            if total > target:
                return
                        
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]: # the i>index is important, it ensure that it won't skip the continous 1 in the recurse, only skip the dups in the loop.
                                                                    #In other word, if removing i > index , the result will miss answer such as [2,2,2] = 6
                    continue
                cur.append(candidates[i])
                dfs(i+1, cur, total+candidates[i])
                cur.pop()

        dfs(0, [], 0)

        return res


# in DFS, i > index and candidates[i] == candidates[i-1] this technique is used to avoid dups




