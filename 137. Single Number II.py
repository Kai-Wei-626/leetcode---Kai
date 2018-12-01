class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maps = {}
        for i in nums:
            maps[i] = 0  # initialize the map
        for i in nums:
            maps[i] += 1
        
        for item in zip(maps.keys(), maps.values()):
            if item[1] == 1:
                return item[0]
