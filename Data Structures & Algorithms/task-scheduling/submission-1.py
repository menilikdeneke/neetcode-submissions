class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency_map = Counter(tasks)
        maxHeap = [-cnt for cnt in frequency_map.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
            