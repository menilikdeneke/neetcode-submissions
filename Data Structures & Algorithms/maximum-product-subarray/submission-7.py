class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = num * curMax

            curMax = max(num, curMin * num, curMax * num)
            curMin = min(num, curMin * num, tmp)

            res = max(res, curMax)
        
        return res