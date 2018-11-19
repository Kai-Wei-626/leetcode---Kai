'''
10 个binary search tree 9 个递归
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.helper(root, -float('inf'), float('inf'))
        else:
            return True
        
    def helper(self, root, min1, max1):
        if root is None:
            return True
        if root.val > min1 and root.val < max1 and self.helper(root.left, min1, root.val) and self.helper(root.right, root.val, max1):
            return True
        else:
            return False
        
        
        
        
        
