'''
deque可以双向pop
迭代终止条件为inorder list为空， 而不是preorder
'''
from collections import deque
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(preorder, inorder):
            if not inorder:
                return None
            
            value = preorder.popleft()
            root = TreeNode(value)
            
            index  = inorder.index(value)
            root.left = helper(preorder, inorder[:index])
            root.right = helper(preorder, inorder[index+1:])
            return root
        
        
        return helper(deque(preorder), inorder)     
            
            
            
            
            
            
            
            
