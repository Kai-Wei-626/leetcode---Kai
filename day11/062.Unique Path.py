'''
重点是要找到规律- 每一个元素都等于上一个和左一个元素的和
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        nums = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            nums[0][i] = 1
        for i in range(n):
            nums[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                nums[i][j] = nums[i-1][j] + nums[i][j-1]
        return nums[n-1][m-1]
#上面的算法中，left most col and top most row initialization can be optimized and combined into the loop after it.


 
#after optimized
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        A=[[0]*n for i in range(m)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    A[j][i]=1
                else:
                    A[j][i]=A[j-1][i]+A[j][i-1]
        return A[j][i]
