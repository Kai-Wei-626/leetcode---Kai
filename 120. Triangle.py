class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        minSum = triangle[-1] 
        
        # from bottom up. curLevel is actuallly the second level to the bottom
        for i in range(len(triangle) - 2, -1, -1):
            curLevel = triangle[i]
            
            for j in range(len(curLevel)):
                minSum[j] = curLevel[j] + min(minSum[j], minSum[j+1])
            
            minSum.pop()
            
        return minSum[0]
                
                
                
