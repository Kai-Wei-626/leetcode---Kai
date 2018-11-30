'''
BFS
同一个level里面可能有多个词，所以在wordlist中这些词都会被remove，this is pretty effective since those word in same level are not expected 
to change to each other. If they can be changed to each other then it's a waste of translation.

另外，每次记得把next_level 清空

https://www.youtube.com/watch?v=vWPCm69MSfs
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        cur_level = [beginWord]  #['cog']
        next_level = []         
        depth = 1
        n = len(beginWord)
        while cur_level:
            for item in cur_level:  # cur_level could have more than 1 item, ex. curword = 'cog', wordlist=['aog','bog'], then both words in wordlist will go to cur_level
                if item == endWord:
                    return depth
                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        word = item[:i] + c + item[i + 1:] 
                        if word in wordList:
                            wordList.remove(word)
                            next_level.append(word)
            depth += 1
            cur_level = next_level
            next_level = []
        return 0

'''
Bidirectional BFS
switch s1, s2 when len(s1) > len(s2) so that only expand the shorter list

firstly, look at if new word is in s2, if failed, then
secondly, look at if new word is in wordList

s1 = s, this operation is same as it in one direction solution.
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict: return 0
        
        l = len(beginWord)
        s1 = [beginWord]
        s2 = [endWord]
        wordDict.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = []  
            for w in s1:
                new_words = [
                    w[:i] + t + w[i+1:]  for t in 'abcdefghijklmnopqrstuvwxyz' for i in range(l)]
                for new_word in new_words:
                    if new_word in s2: return step + 1
                    if new_word in wordDict:
                        wordDict.remove(new_word)                        
                        s.add(new_word)
            s1 = s
        
        return 0    
