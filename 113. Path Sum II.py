'''
add a backtracking logic to both normal operation part and if condition part.
'''

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        cur = []
        res = []
        aggr = 0
        self.helper(root, aggr, sum, cur, res)
        return res
        
    def helper(self, root, aggr, sum, cur, res):
        if root is None:
            return 
        elif root.left is None and root.right is None and aggr + root.val == sum:
            cur.append(root.val)
            res.append(list(cur))
            #backtracking
            cur.pop()
        
        cur.append(root.val)
        aggr = aggr + root.val
        self.helper(root.left, aggr, sum, cur, res)
        self.helper(root.right, aggr, sum, cur, res)
        #backtracking
        cur.pop()
        
        
