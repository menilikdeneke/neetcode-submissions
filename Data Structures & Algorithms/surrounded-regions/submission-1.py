class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            
            board[r][c] = 'T'

            for dr, dc in directions:
                capture(r + dr, c + dc)
            
        
        for i in range(ROWS):
            capture(i, 0)
            capture(i, COLS - 1)
        
        for j in range(COLS):
            capture(0, j)
            capture(ROWS - 1, j)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'