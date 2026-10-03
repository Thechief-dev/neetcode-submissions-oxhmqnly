class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}

        def dfs(amount):
            if amount in self.memo:
                return self.memo[amount]
            if amount == 0:
                return 0
            
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            self.memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= (float('inf')) else minCoins
