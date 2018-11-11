'''
此题难点是确定要用到四个pointer， top, left, right, bot
另外还有最后left = right, top = bot 的情况
'''

#spiral matrix
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        
        ret = []
        left, right, top, bot = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left < right and top < bot:
            for i in range(right - left):
                ret.append(matrix[top][left + i])  #行变量不变， 列变量 + 1
            for i in range(bot - top):
                ret.append(matrix[top + i][right]) #列变量不变， 行变量 + 1
            for i in range(right - left):
                ret.append(matrix[bot][right - i])
            for i in range(bot - top):
                ret.append(matrix[bot - i][left])
            
            left += 1
            right -= 1
            top += 1
            bot -= 1
        
        if left == right: # when left = right, the pointer will only go down
            for i in range(bot - top + 1):
                ret.append(matrix[top + i][left])
        elif top == bot:  # when top = bot, the pointer will only go right
            for i in range(right - left + 1):
                ret.append(matrix[top][left + i])
                
        return ret
        
