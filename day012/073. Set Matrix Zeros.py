'''
need to record the index of 0 place first
then run the helper function. 
'''

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    #record them
                    nums.append([i,j])
        for num in nums:
            i = num[0]
            j = num[1]
            self.helper(matrix, i, j)
        
        
    def    helper(self, matrix, i , j):
            # row 
            for p in range(len(matrix[i])):
                matrix[i][p] = 0
            for q in range(len(matrix)):
                matrix[q][j] = 0
