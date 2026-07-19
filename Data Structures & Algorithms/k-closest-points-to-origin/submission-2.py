class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [-(math.sqrt(x**2 + y**2)) for x, y in points]
        self.maxHeap = [(distance, point) for distance, point in zip(distances, points)]
        heapq.heapify(self.maxHeap)
        res = []

        while len(self.maxHeap) > k:
            heapq.heappop(self.maxHeap)
        
        for pair in self.maxHeap:
            res.append(pair[1])
        
        return res
