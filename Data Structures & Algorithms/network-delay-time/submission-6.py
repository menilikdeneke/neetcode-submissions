class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((t, v))

        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        res = 0
        visit = set()

        while minHeap:
            c1, t1 = heapq.heappop(minHeap)
            if t1 in visit:
                continue
            visit.add(t1)
            res = c1
            for c2, t2 in adj[t1]:
                if t2 not in visit:
                    heapq.heappush(minHeap, (c1 + c2, t2))
        
        return res if len(visit) == n else -1