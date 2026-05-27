class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        for item in nums:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
        for item in frequency:
            if frequency[item] != 1:
                return True
        return False
         