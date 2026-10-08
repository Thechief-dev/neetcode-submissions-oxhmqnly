class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo = {}
        target = sum(nums) // 2
        if sum(nums) % 2:
            return False

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
               
            if (i, target) in memo:
                return memo[(i, target)]
            
            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])

            return memo[(i, target)]

        return dfs(0, target)
                