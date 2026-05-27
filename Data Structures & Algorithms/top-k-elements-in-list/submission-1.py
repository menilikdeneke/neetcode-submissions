class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        freq = {}
        output = []
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        for key, value in freq.items():
            buckets[value].append(key)

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output

        return output 