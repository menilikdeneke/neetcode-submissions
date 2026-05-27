class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        n = len(nums)
        output = [0] * n

        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output