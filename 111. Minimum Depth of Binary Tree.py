'''
the method of this one is easy - calculate the depth of left subtree and right subtree. But when calculating the depth, 
we need to calculate the minumum depth to the nearest leaf node, so we have to add a condition to determine if the node is a 
leaf node.
'''

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        
        if l==0 or r==0:
            return max(l, r) + 1
        
        return min(l, r) + 1
            
        
    def height(self, root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        if root.left and root.right: #to determine if node is a leaf node
            return min(lheight, rheight) + 1
        else:
            return max(lheight,rheight) + 1
        
        
        
        
# clearer solution
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left and root.right is None:
            return 1 + self.minDepth(root.left)
        elif root.right and root.left is None:
            return 1 + self.minDepth(root.right)
        
        
        
