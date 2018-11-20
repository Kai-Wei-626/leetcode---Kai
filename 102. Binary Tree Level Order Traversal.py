'''
第一步： 找到高度。 第二步： bst每搜索到下一层，高度减一，打印条件为高度等于1.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        h = self.height(root) 
        res = []
        
        for i in range(1, h+1):
            cur = []
            self.printNode(root, i, cur)
            res.append(cur)
            
        return res
    
    #https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/    
    #this is really helpful to understand depth funciton
    def height(self, root):
        if root is None:
            return 0
        else:
            lheight = self.height(root.left)
            rheight = self.height(root.right)
            
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
            
    def printNode(self, root, level, cur):
        if root is None:
            return
        if level == 1:
            cur.append(root.val)
        if level > 1:
            self.printNode(root.left, level - 1, cur)
            self.printNode(root.right, level - 1, cur)
        
        
        
