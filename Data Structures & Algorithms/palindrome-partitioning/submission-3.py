class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i, j):
            if j >= len(s):
                if j == i:
                    res.append(part.copy())
                return
            
            if self.isPali(s, i, j):
                part.append(s[i: j + 1])
                dfs(j + 1, j + 1)
                part.pop()
            
            dfs(i, j + 1)
        dfs(0, 0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True