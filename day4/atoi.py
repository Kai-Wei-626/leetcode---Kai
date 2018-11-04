'''
fail solution
not sure how to solve input '+-10'
'''

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        :digit 0 - 9 -> 48 - 57
        """
        INT_MAX, INT_MIN = 2147483647, -2147483648
        result = 0
        sign =1
        for i in range(len(str)):
            #minus_sign = 0
            if str[i] ==' ':
                continue
            if str[i] == '-':
                sign = -1
                continue
            if str[i] in '+-':
                continue
            if str[i].isdigit():
                result = result * 10 + (ord(str[i]) - ord("0")) 
            elif str[i] != ' ' and str[i] != '-' and str[i].isdigit() == False:
                break                
        result = result*sign        
        if sign == 1 and result >= INT_MAX:     
            return INT_MAX
        if sign == -1 and result <= INT_MIN:  

            return INT_MIN
        
        return result
