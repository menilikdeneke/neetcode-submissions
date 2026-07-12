class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        res = []

        for key, val in frequency.items():
            buckets[val].append(key)
        
        for i in range(n, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res