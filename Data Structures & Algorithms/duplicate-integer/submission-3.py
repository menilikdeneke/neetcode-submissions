class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = Counter(nums)

        for num in frequency.keys():
            if frequency[num] > 1:
                return True
        return False