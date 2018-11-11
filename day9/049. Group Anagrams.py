'''
create a dict to save every sorted str
   1. be careful because sorted('abc') = ['a', 'b', 'c'], so use ''.join(sorted(strs[i])) as key of dict
   2. dict won't take a list as key. thats why use join 
then append the unsorted str to the value of dict based on the key which is a sorted list
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict1 = {}
        for i in range(len(strs)):
            dict1[''.join(sorted(strs[i]))] = []
        for i in range(len(strs)):
            dict1[''.join(sorted(strs[i]))].append(strs[i])
        return list(dict1.values())
