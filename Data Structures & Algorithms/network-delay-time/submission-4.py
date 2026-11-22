class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for time in times:
            t0, t1, c = time[0], time[1], time[2]
            adj[t0].append((c, t1))
        
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        visited = set()
        min_c = 0

        while minHeap:
            c1, t1 = heapq.heappop(minHeap)
            if t1 in visited:
                continue
            visited.add(t1)
            min_c = c1
            for c2, t2 in adj[t1]:
                if t2 not in visited:
                    heapq.heappush(minHeap, (c1 + c2, t2))
        
        return min_c if len(visited) == n else -1