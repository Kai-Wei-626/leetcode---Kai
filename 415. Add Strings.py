class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num2 = '0' * (len(num1) - len(num2)) + num2
        else:
            num1 = '0' * (len(num2) - len(num1)) + num1
            
            
        carry = 0
        res = ''
        
        for i in reversed(range(len(num1))):
            num  = int(num1[i]) + int(num2[i]) + carry # add 2 numbers together plus carry
            
            res = str(num)[-1] + res # add the cur str to the result
            
            if num > 9:
                carry = 1
            else:
                carry = 0
                
        if carry == 1:
            res = '1' + res
            
        return res
            
            
            
