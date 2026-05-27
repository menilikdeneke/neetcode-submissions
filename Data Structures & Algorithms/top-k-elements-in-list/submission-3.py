class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for i in range(n + 1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num in count:
            freq[count[num]].append(num)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res