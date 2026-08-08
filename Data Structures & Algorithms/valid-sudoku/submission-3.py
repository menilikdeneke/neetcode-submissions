class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r//3, c//3)]):
                    return False
                if board[r][c] == '.':
                    continue
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        
        return True