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

                
## change the value on one loop, but not change to 0 direct becuase that will cause other places to become zero which will 
# lead to extra unnecessary zero. so to avoid that from happending, we change them to a string value.
# after the first loop has finished, we replace all the string with 0
# save the space but time complexicity changed from O(mn) to O(2mn)
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    #record them
                    self.helper(matrix, i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
                    
        
    def    helper(self, matrix, i , j):
            # row 
            for p in range(len(matrix[i])):
                if matrix[i][p] != 0:
                    matrix[i][p] = 'a'
            for q in range(len(matrix)):
                if matrix[q][j] != 0:
                    matrix[q][j] = 'a'            
