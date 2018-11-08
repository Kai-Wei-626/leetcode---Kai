'''
([board[row+i][col+j] for i in range(3) for j in range(3)]) -------- very fancy expression
'''

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for col in range(9):
            if self.hasDup([board[row][col] for row in range(9)]):
                return False
            
        for row in range(9):
            if self.hasDup(board[row]):
                return False
            
        for row in [0,3,6]:
            for col in [0,3,6]:
                if self.hasDup([board[row+i][col+j] for i in range(3) for j in range(3)]):
                    return False
            
        return True
    
    def hasDup(self, l):
        ret = []
        for i in range(len(l)):
            if l[i] != '.':
                if l[i] in ret:
                    return True
                else:
                    ret.append(l[i])
        return False
            
        
