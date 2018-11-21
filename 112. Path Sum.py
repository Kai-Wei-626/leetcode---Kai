'''
1. be careful of negtive number
2. understand the question, the path sum is the summation of the all node between root node and leaf node, which means a 
subset of its path won't apply
'''
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.helper(root, 0, sum)
    
    
    def helper(self, root, aggr, sum):
        if root is None:
            return False
        elif root.left is None and root.right is None and aggr + root.val == sum:
            return True
        #print(root.val, aggr)
        return self.helper(root.left, aggr + root.val, sum) or self.helper(root.right, aggr + root.val, sum)
            
        
