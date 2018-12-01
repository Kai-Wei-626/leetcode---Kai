'''
dfs, be careful with case [1,2,3,null,4]
'''
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = []
        cur = ''
        self.helper(root, cur, res)
        return sum(res)
        
    def helper(self, root, cur, res):
        if root is None:
          return 
        
        if root and not root.left and not root.right:
            res.append(int(cur + str(root.val)))
            return
            
        cur = cur + str(root.val)

        self.helper(root.left, cur, res)
        self.helper(root.right, cur, res)


        
'''
res needs to be [0], if set res = 0, it won't work
'''
class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [0]
        cur = 0
        self.helper(root, cur, res)
        return res[0]
        
    def helper(self, root, cur, res):
        #print(cur, res)
        if root is None:
            return 

        if root.left is None and root.right is None:
            res[0] += cur * 10 + root.val
            return

        cur = cur*10 + root.val

        self.helper(root.left, cur, res)
        self.helper(root.right, cur, res)
        
        
        
