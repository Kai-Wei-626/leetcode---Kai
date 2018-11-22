'''
画图找规律，想办法嫁接
'''
class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #因为是preorder traversal -> so 
        
        if root is None:
            return
        #step1
        if root.left:
            end = root.left
            while end.right:
                end = end.right
            end.right = root.right
            #step2
            root.right = root.left
            root.left = None
        root = root.right
        self.flatten(root)
            
            
            
