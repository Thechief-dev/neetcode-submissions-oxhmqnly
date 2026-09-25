class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo ={}

        def dfs(n):
            if n <= 2:
                return n
            if n in self.memo:
                return self.memo[n]

            self.memo[n] = dfs(n - 1) + dfs(n - 2)
            return self.memo[n]

        return dfs(n)
