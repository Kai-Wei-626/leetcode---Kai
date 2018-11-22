class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        matrix = [[] for i in range(numRows)]
        matrix[0].append(1)
        
        for i in range(1, numRows):
            matrix[i].append(1)
            for j in range(1, i):
                matrix[i].append(matrix[i-1][j-1] + matrix[i-1][j])
            matrix[i].append(1)
        
        return matrix
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
