'''
这道题目是102的变形， 但是我的102solution里面用的是递归，而这里用的是iteration。 详情参考geekforgeeks。 代码url如下，非常清晰
https://www.geeksforgeeks.org/level-order-tree-traversal/
唯一的区别是，url里面的代码是按照顺序打印，而本题需要将每一层的val用list的形式答应并且append到res里面


对于below代码其实不需要import deque， python的list可以使用insert(0, val)。。。 稍微改一下，见solution2
'''

from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # a queue that can put in nodes 
        if root is None:
            return []
        res = []
        queue = deque([])
        
        queue.append(root)
        
        while len(queue) > 0:
            cur = []
            for i in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.insert(0, cur)
        return res
        
#solution2

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # a queue that can put in nodes 
        if root is None:
            return []
        res = []
        queue = []
        
        queue.append(root)
        
        while len(queue) > 0:
            cur = []
            for i in range(len(queue)):
                node = queue.pop()
                cur.append(node.val)
                if node.left:
                    queue.insert(0,node.left)
                if node.right:
                    queue.insert(0,node.right)
            
            res.insert(0, cur)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
