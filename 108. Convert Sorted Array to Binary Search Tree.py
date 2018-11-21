'''
这题要满足两个条件：
1. 每一个node下的subtree必须是height balanced
2. 必须是
'''

class Solution(object):
    def sortedArrayToBSTHelper(self, nums, first, last):
        if first>last:
            return None

        mid = (first + last)//2
        
        ret = TreeNode(nums[mid])
        ret.left  = self.sortedArrayToBSTHelper( nums, first, mid-1 )
        ret.right = self.sortedArrayToBSTHelper( nums, mid+1, last  )

        return ret

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTHelper(nums, first=0, last=len(nums)-1)
