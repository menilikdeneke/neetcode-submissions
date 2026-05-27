class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))
        return max_area