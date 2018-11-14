'''
be awared that, if condition else something only apply when using on i += 1
it's confusing
just use normal if: 
                else: statement
'''
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ret = ''
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        while m >= 0 or n >= 0 or carry == 1: 
            carry += int(a[m]) if m >= 0 else 0
            carry += int(b[n]) if n >= 0 else 0
            ret = str(carry%2) + ret
            carry = carry//2
            m, n = m-1, n-1
            
        return ret
            

         
            
