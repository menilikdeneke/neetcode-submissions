class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        atl = set()
        pac = set()
        res = []

        def dfs(r, c, prev, visit):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[r][c] < prev or (r, c) in visit:
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visit)
        
        for i in range(ROWS):
            dfs(i, 0, heights[i][0], pac)
            dfs(i, COLS - 1, heights[i][COLS - 1], atl)
        
        for j in range(COLS):
            dfs(0, j, heights[0][j], pac)
            dfs(ROWS - 1, j, heights[ROWS - 1][j], atl)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl and (r, c) not in res:
                    res.append((r, c))
        return res
