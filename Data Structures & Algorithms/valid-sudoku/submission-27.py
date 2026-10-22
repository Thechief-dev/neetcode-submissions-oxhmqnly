class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        unique = set()
        for i in range(9):
            unique = set()
            for r in range(rows):
                
                if board[r][i] in unique:
                    return False
                if board[r][i] == '.':
                    continue
                unique.add(board[r][i])
        for i in range(9):
            unique = set()
            for c in range(cols):
                if board[i][c] in unique:
                    return False
                if board[i][c] == '.':
                    continue
                unique.add(board[i][c])
        for square in range(9):
            unique = set()
            for i in range(3):
                for j in range(3):
                    rows = (square // 3) * 3 + i
                    cols = (square % 3) * 3 + j
                    if board[rows][cols] == '.':
                        continue
                    if board[rows][cols] in unique:
                        return False
                    unique.add(board[rows][cols])
        return True
            
