'''
create a list ret = ['0'], append {[(, when }]) and match with list[-1], pop
make sure ret list is not empty, since it will meet out of indice error. and don't forget to add that to the mapping dict.
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict1 = {'{':'}','[':']','(':')','0':'0'}
        ret = ['0']
        if s == '':
            return True
        for i in range(len(s)):
            if s[i] in '{[(':
                ret.append(s[i])
            elif s[i] in '}])' and dict1[ret[-1]] == s[i]:
                ret.pop()
            else:
                return False

                
        if ret == ['0']:
            return True
        else:
            return False
                
        
        
        
        
        
            
