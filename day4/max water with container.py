# brute force
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
        
        
        
#solution 2, 2 pointer
'''
the whole idea of this algo is that by comparing the values of left pointer and right pointer, while one of them is lower 
or equal to the other, that one moves. it is something like you have to give the chance to that pointer to look for next taller
bar, the distance between two pointers is always decreasing, so don't need to worry about it.
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxArea = 0
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        
