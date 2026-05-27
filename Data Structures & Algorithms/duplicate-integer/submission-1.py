class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                return True

        return False       