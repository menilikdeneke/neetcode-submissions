class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if min(r, c) < 0 or r >= ROWS or c >= COLS or ((r, c) in seen) or board[r][c] != word[i]:
                return False
            
           
            seen.add((r, c))

            res = (dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r ,c - 1, i + 1))
            seen.remove((r, c))
            return res
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False