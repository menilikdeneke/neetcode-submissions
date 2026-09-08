class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num, num * curMin, num*curMax)
            curMin = min(tmp, num * curMin, num)
        
            res = max(curMax, res)
        return res