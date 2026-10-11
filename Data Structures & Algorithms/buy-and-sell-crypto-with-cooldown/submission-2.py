class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(i, tradeIn):
            if (i, tradeIn) in memo:
                return memo[(i, tradeIn)]
            if i >= len(prices):
                return 0

            cooldown = dfs(i + 1, tradeIn)

            if tradeIn:
                buy = dfs(i + 1, not tradeIn) - prices[i]
                memo[(i, tradeIn)] = max(buy, cooldown)
                return memo[(i, tradeIn)]
            else:
                sell = dfs(i + 2, not tradeIn) + prices[i]
                memo[(i, tradeIn)] = max(sell, cooldown)
                return memo[(i, tradeIn)]
        return dfs(0, True)

