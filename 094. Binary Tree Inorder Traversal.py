# recursion solution
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        
        if root:
            
            self.helper(root.left, res)
            
            res.append(root.val)
            
            self.helper(root.right, res)
 
 
# iterative solution
# 逻辑非常巧妙
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        done = True
        if root is None:
            return []
        curr = root
        while done:
            #go to leftmost node
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                #backwards one step
                if len(stack) >0:
                    curr = stack.pop() 
                    res.append(curr.val) 
                    curr = curr.right
                else:
                    done = False
        return res
            
