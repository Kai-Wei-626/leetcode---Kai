class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        binary search in first col
        binary search in the row
        '''
        
        # find the row, critiria: target > row and target < row + 1
        if matrix == [] or matrix == [[]]:
            return False
        left = 0 
        right = len(matrix) - 1
        while left <= right:
            
            mid = (left + right) // 2
            #print(left, right, mid)
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                left = mid + 1
            if matrix[mid][0] > target:
                right = mid - 1 
        
        #so left - 1 is the row number
        row = left - 1
        # if the element is less than m[0][0], then reutrn false
        if row <0:
            return False
        
        left, right = 0, len(matrix[0])-1
        
        while left <= right:
            mid = (left + right)//2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid -1
            if matrix[row][mid] < target:
                left = mid + 1
        
        return False
        
        
        
