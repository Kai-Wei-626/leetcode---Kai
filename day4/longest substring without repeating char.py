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
    
    
#sliding window 
'''
https://www.youtube.com/watch?v=9VcYiqTqzUY
解释的很好

below are important tips
1. initialize a counter with -1, switch to 1 when no duplicate
2. when having duplicate, start left, find the duplicate in the sliding window.
3. Don't forget to compare maxlen and right - left in the end, otherwise you won't pass test case 'aaaa'.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        n = len(s)
        left = 0
        right = 0
        maxlen = 0
        counts = [-1]*128
        while right < n:
            if counts[ord(s[right])] == -1:
                counts[ord(s[right])] = 1
                right += 1
            else:
                while (left < right) and (s[right] != s[left]):
                    maxlen = max(maxlen, right - left)
                    counts[ord(s[left])] = -1
                    left += 1
                left += 1
                right += 1
        return max(maxlen, right - left)
                    
