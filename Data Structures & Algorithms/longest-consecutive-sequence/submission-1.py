class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                n = 1
                curr = nums[i]
                while curr + 1 in num_set:
                    curr += 1
                    n += 1
                
                longest = max(longest, n)
        
        return longest