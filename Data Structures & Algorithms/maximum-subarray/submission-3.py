class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, total = nums[0], 0
        for num in nums:
            if total < 0:
                total = num
            else:
                total += num
            maxSub = max(total, maxSub)
        return maxSub   