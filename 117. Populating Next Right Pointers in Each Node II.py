      
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
      if not root:
        return None

      q = deque([root])
      
      while q:
        # Each time update the length of q
        N = len(q)
        for _ in range(N):
          node = q.popleft()
          if node.left:
            q.append(node.left)
          
          if node.right:
            q.append(node.right)
        
        
        # Update the relationship between each node
        if len(q) > 1:
          for i in range(len(q)-1):
            q[i].next = q[i+1]
          
            
