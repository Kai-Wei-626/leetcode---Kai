'''
best explanation: https://www.youtube.com/watch?v=oUeGFKZvoo4
DFS CLASSIC
used matrix is actually unnesscary. We can assign the curr value to a number.
couple points need taking attention:
1. out of boundary check has to come fisrt in the helper function 
2. Don't forget backtracking.
3. d is recursion depth. len(word) has to equal to d + 1 to return Ture.

'''

class Solution:
    def exist(self, board, word):
        d = 0
        used = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                #print(i,j)
                #used = [[False for j in range(len(board[0]))] for i in range(len(board))]
                if self.search(board, word, d, i, j, used): 
                    return True
        return False

    # d is recursion depth
    def search(self, board, word, d, i, j, used):
        #print(d,i,j,used)
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0]) - 1:
            return False
        
        if used[i][j]:
            return False

        if board[i][j] != word[d]:
            return False

        if len(word) == d+1:
            return True

        used[i][j] = True
        found = self.search(board, word, d+1, i-1, j,used) or self.search(board, word, d+1, i+1, j,used) or self.search(board, word, d+1, i, j-1,used) or self.search(board, word, d+1, i, j+1,used)
        used[i][j] = False
        return found
