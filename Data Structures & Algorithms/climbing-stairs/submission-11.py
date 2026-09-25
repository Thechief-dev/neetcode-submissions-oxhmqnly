class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}

        def helper(n, memo):

            if n in memo:
                return memo[n]

            if n <= 2:
                return n

            memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
            return memo[n]
        return helper(n, {})