class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)
            if first_stone < second_stone:
                heapq.heappush(stones, first_stone - second_stone)
        
        stones.append(0)
        return abs(stones[0])