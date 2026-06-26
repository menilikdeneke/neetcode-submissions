class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        atl = set()
        pac = set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if c < 0 or r < 0 or r >= ROWS or c >= COLS or heights[r][c] < prevHeight or (r, c) in visit:
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        
        return res