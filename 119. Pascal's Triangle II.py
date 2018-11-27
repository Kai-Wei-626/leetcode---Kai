class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nums = [1]
        
        for i in range(rowIndex):
            newNums = [1]
            for j in range(1, len(nums)):
                newNums.append(nums[j-1] + nums[j])
            newNums.append(1)
            
            nums = newNums
            
        return nums
        
        
        
        
