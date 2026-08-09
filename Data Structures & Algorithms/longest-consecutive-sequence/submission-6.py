class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                length = 0
                curr = num
                while curr in numSet:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        
        return longest