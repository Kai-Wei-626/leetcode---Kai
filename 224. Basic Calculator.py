class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sign = 1
        i = 0
        stack = []
        while i < len(s):
        	c = s[i]
        	if c.isdigit():
        		num = 0
        		while i < len(s) and s[i].isdigit():
        			num = num * 10 + int(s[i])	
        			i += 1
        		res += sign * num
        		continue

        	elif c == '+':
        		sign = 1
        	elif c == '-':
        		sign = -1
        	elif c == '(':
        		stack.append(res)                  # push previous res into the stack as in parenthese value need to be calc first
        		stack.append(sign)				   # push sign before the open parenthese 
        		res = 0
        		sign = 1
        	elif c == ')':
        		res *= stack.pop()
        		res += stack.pop()
        	i += 1
            
        return res
