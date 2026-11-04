class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        minHeap = []

        for u, v, t in times:
            adj[u].append((t, v))
        
        minHeap.append((0, k))

        heapq.heapify(minHeap)

        visited = set()

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = t1

            for t2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (t2 + time, n2))
        
        return time if len(visited) == n else -1
