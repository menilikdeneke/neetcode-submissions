class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            cur = self.parent[cur]
            self.parent[cur] = self.parent[self.parent[cur]]
        return cur
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)
        for edge in edges:
            if dsu.union(edge[0], edge[1]):
                res -= 1
        return res