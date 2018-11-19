# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.helper(p,q)
        
    def helper(self, p, q):
        if p is None and q is None:
            return True
            
        elif p is not None and q is not None and p.val == q.val:
            return self.helper(p.left, q.left) and self.helper(p.right, q.right)
        
        else:
            return False
