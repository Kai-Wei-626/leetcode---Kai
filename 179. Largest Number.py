class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums1 = []
        for i in range(len(nums)):
            nums1.append(str(nums[i]))
        
        #change the way of sort -- not base on the which is heigher of x and y, but based on the number of x + y and y + x
        compare = lambda x, y: 1 if x+y < y+x else -1 if x+y > y+x else 0
        
        nums1.sort(cmp = compare)
        
        return str(int(''.join(nums1)))
