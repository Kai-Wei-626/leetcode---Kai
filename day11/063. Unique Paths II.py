'''
1. fill first row, if nums[][] == 1, all elements after itself(inclusive) is 0
2. fill first col, the algo is same as above
3. except first row first col, any encoutered nums[][] = 1, we just change it to 0
4. watch the special case that when nums[0][0] == 1. return 0
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid[0]) #7
        n = len(obstacleGrid) #3
        if obstacleGrid[0][0] == 1:
            return 0
        
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                for p in range(i, m):
                    obstacleGrid[0][p] = 0
                break
            else:
                obstacleGrid[0][i] = 1

        ## fix num[0][0] element, otherwise the next loop will make leftmost col with 0
        obstacleGrid[0][0] = 0
        
        for j in range(n):
            if obstacleGrid[j][0] == 1:
                for p in range(j, n):
                    obstacleGrid[p][0] = 0
                break
            else:
                obstacleGrid[j][0] = 1
         
        for i in range(1, n):
            for j in range(1, m):
                    if obstacleGrid[i][j] == 1:
                        obstacleGrid[i][j] = 0
                        continue
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[n-1][m-1]
                                
