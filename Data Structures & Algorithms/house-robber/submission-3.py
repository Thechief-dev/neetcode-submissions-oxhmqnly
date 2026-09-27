class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo ={}
        def dfs(i):
            if i in self.memo:
                return self.memo[i]
            if i >= len(nums):
                return 0
            self.memo[i] = max (dfs(i + 1), nums[i] + dfs(i + 2))
            return self.memo[i]
            
        return dfs(0)