class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, isBuyCoin):
            if (i, isBuyCoin) in memo:
                return memo[(i, isBuyCoin)]
            if i >= len(prices):
                return 0

            if isBuyCoin:
                buy = dfs(i + 1, not isBuyCoin) - prices[i]
                cooldown = dfs(i + 1, isBuyCoin)
                memo[(i, isBuyCoin)]= max(buy, cooldown)
            else:
                sell = dfs(i + 2, not isBuyCoin) + prices[i]
                cooldown = dfs(i + 1, isBuyCoin)
                memo[(i, isBuyCoin)] = max(sell, cooldown)

            return memo[(i, isBuyCoin)]

        return dfs(0, True)
