class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        
        for pre, crs in edges:
            adj[crs].append(pre)
            adj[pre].append(crs)
        
        cycle = set()

        def dfs(crs, par):
            if crs in cycle:
                return False
            
            cycle.add(crs)

            for nei in adj[crs]:
                if nei == par:
                    continue
                if not dfs(nei, crs):
                    return False
            return True
        
        return dfs(0, -1) and len(cycle) == n