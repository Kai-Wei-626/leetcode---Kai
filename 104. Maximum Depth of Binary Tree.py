#先recursion到底， 然后再往上面上升，然后得到高度
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            lheight = self.maxDepth(root.left)
            rheight = self.maxDepth(root.right)
            
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
            
            
            
            
