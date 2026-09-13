class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes_to_edges = {i : [] for i in range(n)}

        for edge in edges:
            nodes_to_edges[edge[0]].append(edge[1])
            nodes_to_edges[edge[1]].append(edge[0])
        visit, cycle = set(), set()
        def dfs(node, parent):
            if node in visit:
                return True
            if node in cycle:
                return False

            cycle.add(node)

            for nei in nodes_to_edges[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            cycle.remove(node)
            visit.add(node)
            return True
        
        if not dfs(0, -1):
            return False
        return len(visit) == n