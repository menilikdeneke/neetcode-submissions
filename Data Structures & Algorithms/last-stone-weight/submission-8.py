class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-s for s in stones]
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > 1:
            x = heapq.heappop(self.maxHeap)
            y = heapq.heappop(self.maxHeap)

            if x < y:
                new_stone = x - y
                heapq.heappush(self.maxHeap, new_stone)
        
        return abs(self.maxHeap[0]) if len(self.maxHeap) > 0 else 0