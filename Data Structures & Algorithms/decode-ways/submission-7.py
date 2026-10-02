class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        def dfs(i):
            if i in self.memo:
                return self.memo[i]
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            res = dfs(i + 1) # getting first index

            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2) # getting first 2 idx
            self.memo[i] = res # No need to travel all possibilities. 
            # just for 1 can able to travel 0,1,2,3,4,5,6,7,8,9 and each will be same process, it will take amazing time and then it will throw exception because of it.
            return self.memo[i]
        return dfs(0)