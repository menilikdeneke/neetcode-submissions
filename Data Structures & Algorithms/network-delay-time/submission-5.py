class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for t1, t2, c in times:
            adj[t1].append((c, t2))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            c1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = c1
            visit.add(n1)
            for c2, n2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (c1 + c2, n2))
        
        return t if len(visit) == n else -1
        