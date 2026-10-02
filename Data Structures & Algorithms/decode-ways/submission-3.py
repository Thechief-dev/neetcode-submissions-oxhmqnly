class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        def dfs (i):
            if i in self.memo:
                return self.memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i < len(s) -1 :
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2)
            self.memo[i] = res
            return res

        return dfs(0)