'''
便利每个node， 并且求出该点left subtree 和 right subtree的height，进行比较。
time： O(n*n)??? 不太会算时间复杂度，感觉是O(n*n)
'''

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
            
        l = self.height(root.left)
        r = self.height(root.right)

        return abs(l-r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)     
        
    def height(self, root):
        if root is None:
            return 0
        lheight = self.height(root.left) + 1
        rheight = self.height(root.right) + 1
        
        return max(lheight, rheight)
    
        
    
        
