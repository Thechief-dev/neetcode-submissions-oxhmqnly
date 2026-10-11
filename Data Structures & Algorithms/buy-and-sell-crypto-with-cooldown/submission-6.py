class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, isSellCoin):
            if (i, isSellCoin) in memo:
                return memo[(i, isSellCoin)]
            if i >= len(prices):
                return 0

            if isSellCoin:
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, isSellCoin)
                memo[(i, isSellCoin)]= max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, isSellCoin)
                memo[(i, isSellCoin)] = max(sell, cooldown)

            return memo[(i, isSellCoin)]

        return dfs(0, True)
