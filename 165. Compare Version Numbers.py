# special case: 1.0 and 1, suppose to return 0 since it's equal -> remove all zero in the end of the list

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')

        maxlen = max(len(version1), len(version2))
        for i in range(maxlen):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0
            
            if v1>v2:
                return 1
            elif v1<v2:
                return -1
            
        return 0
