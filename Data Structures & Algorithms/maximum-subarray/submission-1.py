class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = 0
        maxSub = nums[0]

        for num in nums:
            curSum = max(num, curSum + num)
            maxSub = max(maxSub, curSum)
        return maxSub