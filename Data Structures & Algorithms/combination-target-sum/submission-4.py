class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            current_sum = sum(subset)
            if current_sum == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or current_sum > target:
                return
        
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res