class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            adding = dfs(i + 1, total + nums[i])
            subs = dfs(i + 1, total - nums[i])

            memo[(i, total)] = adding + subs
            return memo[(i, total)]
        return dfs(0, 0)