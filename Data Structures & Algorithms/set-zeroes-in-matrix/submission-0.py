class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])

        mark_rows, mark_cols = [False] * rows, [False] * cols

        for r in range(rows):
            for c in  range(cols):
                if matrix[r][c] == 0:
                    mark_rows[r] = True
                    mark_cols[c] = True

        for r in range(rows):
            for c in range(cols):
                if mark_rows[r] or mark_cols[c]:
                    matrix[r][c] = 0