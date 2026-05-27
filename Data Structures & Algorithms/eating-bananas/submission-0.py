class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_rate = r

        while l <= r:
            k = (l + r) // 2
            hrs = 0
            for num in piles:
                hrs += math.ceil(num/k)
            if hrs > h:
                l = k + 1
            else:
                min_rate = k
                r = k - 1

        
        return min_rate