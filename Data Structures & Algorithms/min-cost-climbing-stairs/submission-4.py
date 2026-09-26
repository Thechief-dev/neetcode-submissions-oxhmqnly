class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        def dfs(i):
            if i in self.memo:
                return self.memo[i]
            if i >= len(cost):
                return 0

            self.memo[i] =cost[i] + min(dfs(i + 1), dfs(i + 2))
            return self.memo[i]
        return min(dfs(0), dfs(1))