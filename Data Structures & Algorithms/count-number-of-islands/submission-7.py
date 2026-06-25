class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count