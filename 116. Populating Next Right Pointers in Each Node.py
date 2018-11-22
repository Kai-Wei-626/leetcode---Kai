'''
第一个循环是while root.left: , 即遍历所有leftmost node
第二个循环是遍历所有同一层的节点， 通过root.next, 但是为了不污染root节点的指向，创建一个新节点cur代替root
     1                      1  
    ／\                    ／\
    2 3         --->       2->3                 root.left.next = root.right
   /\ /\                  /\ /\
  4 5 6 7                4 5 6 7
  
     1                      1  
    ／\                    ／\
    2 3         --->      2  3                   
   /\ /\                  /\ /\
  4 5 6 7                4 5 6 7
 
 如何链接5和6？ 此时root为2，故用，root.right.next = root.next.left, 
 at the same time, connect 6 and 7 by using root.next.left.next = root.next.right
  
  
'''


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        
        if root is None:
            return
        #the first node of every level is the root node
        while (root.left): 
            root.left.next = root.right
            cur = root
            while cur.next:
                cur.right.next = cur.next.left
                cur.next.left.next = cur.next.right
                cur = cur.next
            root = root.left
            
        
        
        
        
        
