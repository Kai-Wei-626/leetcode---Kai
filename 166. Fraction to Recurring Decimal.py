class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0: return str(numerator // denominator)
        p, q = map(abs, (numerator,denominator)) #apply abs function on p,q
        prefix = ('' if ((numerator > 0) == (denominator > 0)) else '-') + str(p//q) + '.'  # everything before the decimal point
        suffix = ''
        remainder = p % q
        index = {}  # use the map to record the position that first recurrence happened

        while remainder not in index:
            index[remainder] = len(suffix) 
            suffix += str(remainder * 10 // q)
            remainder = remainder * 10 % q
            if remainder == 0: return prefix + suffix # no recurring suffix

        return prefix + suffix[: index[remainder]] + '(' + suffix[index[remainder]:] + ')'

s = Solution()
s.fractionToDecimal(4, 333)
