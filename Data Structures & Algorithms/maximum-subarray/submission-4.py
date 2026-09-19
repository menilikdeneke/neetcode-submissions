class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = float('-inf')
        final = float('-inf')

        for num in nums:
            curSum += num
            curSum = max(curSum, num)
            final = max(final, curSum)
        
        return final