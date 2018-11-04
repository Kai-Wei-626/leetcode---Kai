'''
zigzag
此方法非常好理解，就是按照zigzag的写法将不同的字符写入对应的组，当指针遇到currow = 0 or numRows -1的组时，方向变相。
'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        retList = [[] for i in range(numRows)]
        direction  = 1
        curRow = 0
        for i in range(len(s)):
            retList[curRow].append(s[i])
            curRow += direction
            if curRow in (0, numRows - 1):
                direction *= -1
        
        retList2 = [0]*numRows
            
        for i in range(len(retList)):
            retList2[i] = ''.join(retList[i])
        return ''.join(retList2)


'''
solution 2
利用数学方法即找规律
'''

#solution 2， use math
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        retList = [[] for i in range(numRows)]
        group = 2 * numRows - 2
        for i in range(len(s)):
            remainder = i % group
            if remainder < numRows:
                retList[remainder].append(s[i])
            else:
                retList[group - remainder].append(s[i])
        
        retList2 = [0]*numRows
            
        for i in range(len(retList)):
            retList2[i] = ''.join(retList[i])
        return ''.join(retList2)        

