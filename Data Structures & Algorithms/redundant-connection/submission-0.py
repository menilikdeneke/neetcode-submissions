class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        
        def find(node):
            cur = node
            while cur != par[node]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            
            if rank[pu] > rank[pv]:
                par[pv] = pu
                rank[pu] += rank[pv]
            else:
                par[pu] = pv
                rank[pv] += rank[pu]
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]