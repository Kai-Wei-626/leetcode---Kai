'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

#brute force
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        
        maxlen = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.uniqueString(s,i,j) and (j-i+1) > maxlen:
                    #print(s[i:j+1])
                    maxlen = j - i + 1
        return maxlen
    def uniqueString(self, s, i, j):
        box = []
        for c in s[i:j+1]:
            if c in box:
                return False
            else:
                box.append(c)
        return True
