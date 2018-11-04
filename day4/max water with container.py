class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                minimal_h = min(height[i], height[j])
                length = j -i
                area = minimal_h * length
                max_area = max(area, max_area)
        return max_area
        
        
        
