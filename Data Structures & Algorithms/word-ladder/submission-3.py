class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        rows, cols = len(wordList), len(wordList[0])
        eachWord = [[] for _ in range(rows)]
        mp = {}

        for i in range(rows):
            mp[wordList[i]] = i

        for i in range(rows):
            for j in range(i + 1, rows):
                count = 0
                for k in range(cols):
                    if wordList[i][k] != wordList[j][k]:
                        count += 1
                if count == 1:
                    eachWord[i].append(j)
                    eachWord[j].append(i)

        q, res = deque(), 1
        visit = set()
        for i in range(cols):
            for c in range(97, 123): # ascii
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i + 1:]

                if word in mp and mp[word] not in visit:
                    q.append(mp[word])
                    visit.add(mp[word])
        
        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                
                for nei in eachWord[node]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
                        

        return 0
            