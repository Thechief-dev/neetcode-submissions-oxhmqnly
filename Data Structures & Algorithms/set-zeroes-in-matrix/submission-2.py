class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        mark_r = [False] * rows
        mark_c = [False] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    mark_r[r] = True
                    mark_c[c] = True
        
        for r in range(rows):
            for c in range(cols):
                if mark_r[r] or mark_c[c]:
                    matrix[r][c] = 0