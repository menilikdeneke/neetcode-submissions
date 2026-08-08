class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numSet = set(nums)

        for num in nums:
            length = 0
            if num - 1 not in numSet:
                cur = num
                while cur in numSet:
                    cur += 1
                    length += 1
                longest = max(length, longest)
        
        return longest