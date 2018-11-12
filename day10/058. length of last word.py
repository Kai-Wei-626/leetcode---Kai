
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) >= 1:
            word_list = s.strip().split(" ")
            last_word = word_list[-1]
            word_count = len(last_word)
            return word_count
        else:
            return 0
            
            

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = 0
        s = s.strip()
        for i in reverse(range(len(s))):
            if s[i] == ' ':
                break
            nums += 1
            
        return nums

             
