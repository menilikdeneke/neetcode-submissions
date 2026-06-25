class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def rot(r, c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        minute = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rot(r + dr, c + dc)
            minute += 1
        
        return minute if fresh == 0 else -1