class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for x in range(n)] for y in range(n)] 
        left, right, top, bot = 0, n-1, 0, n-1   
        num = 1
        while left < right and top < bot:
            for i in range(right - left):
                matrix[top][left + i] = num
                #print(top, left + i, num)
                num += 1
            for i in range(bot - top):
                matrix[top + i][right] = num
                #print(top + i, right,num)
                num += 1
            for i in range(right - left):
                matrix[bot][right - i] = num
                #print(bot, right - i,num)
                num += 1
            for i in range(bot - top):
                matrix[bot - i][left] = num
                #print(bot - i, left,num)
                num += 1
            left += 1
            right -= 1
            top += 1
            bot -= 1
           
        if left == right: # when left = right, the pointer will only go down
            for i in range(bot - top + 1):
                matrix[top + i][left] = num
                num += 1
        elif top == bot:  # when top = bot, the pointer will only go right
            for i in range(right - left + 1):
                matrix[top][left + i] = num
                num += 1                             
        return matrix
        
