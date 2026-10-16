class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        def dfs(r, c, prevVal):
            if (r,c, prevVal) in memo:
                return memo[(r,c,prevVal)]
            if r >= rows or c >= cols or r < 0 or c < 0 or matrix[r][c] <= prevVal:
                return 0
            res = 1

            right = 1 + dfs(r + 1, c, matrix[r][c])
            left = 1 + dfs(r - 1, c, matrix[r][c])
            top= 1 + dfs(r, c + 1, matrix[r][c])
            bottom = 1 + dfs(r , c - 1, matrix[r][c])
            res = max(max(max(left, right), top),bottom)
            memo[(r,c,prevVal)] = res
            return memo[(r,c,prevVal)]
        maxi = 0
        for r in range(rows):
            for c in range(cols):
                maxi= max(maxi, dfs(r, c, float('-inf')))
        return maxi