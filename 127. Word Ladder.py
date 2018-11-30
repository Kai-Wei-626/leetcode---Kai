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
