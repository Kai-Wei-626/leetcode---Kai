'''
先沿着 竖着的 中轴 对换元素，记住加限制条件，不然会换了两遍结果啥也没变
再沿着bottom left to top right direction 变换元素
‘’‘

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        #flip over the vertical middle line

        n = len(matrix)
        mid = n//2
        for i in range(n):
            for j in range(mid):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
        #flip over the diagonal line
        for i in range(n):
            for j in range(n):
                if i+j < n:
                    matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
                    
        
                    
