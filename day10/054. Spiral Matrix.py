#spiral matrix
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        left, right, top, bot = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left < right and top < bot:
            for i in range(right - left):
                ret.append(matrix[left][i])
            for i in range(bot - top):
                ret.append(matrix[i][right])
            for i in range(right - left):
                ret.append(matrix[bot][right - i])
            for i in range(bot - top):
                ret.append(matrix[bot - i][left])
            
            left += 1
            right -= 1
            top += 1
            bot -= 1
        
        if left == right: # when left = right, the pointer will only go down
            for i in range(bot - top + 1): # bot - top + 1, otherwise i = null
                ret.append(matrix[top + i][left])
        elif top == bot:  # when top = bot, the pointer will only go right
            for i in range(right - left + 1):
                ret.appedn(matrix[top][left + i])
                
        return ret
        
m =[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

s = Solution()
s.spiralOrder(m)
