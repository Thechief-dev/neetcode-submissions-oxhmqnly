class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2,-1, -1):
                newRow[j] = newRow[j + 1] + row[j] # same like continous ops not directly recursive but same operation with old value.
            row = newRow # new row values in row becuase we are going to use for next iter.
        return row[0]
        
