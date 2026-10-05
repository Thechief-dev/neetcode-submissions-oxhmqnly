class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        def dfs(i):
            if i in self.memo:
                return self.memo[i]
            if i == len(s):
                return True
            for word in wordDict:
                if word == s[i : i + len(word)]:
                    if dfs(i + len(word)) == True:
                       self.memo[i] = True
                       return True
            self.memo[i] = False
            return False
        return dfs(0)


