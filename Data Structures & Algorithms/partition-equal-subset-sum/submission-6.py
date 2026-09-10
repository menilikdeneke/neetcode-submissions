class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        memo = [[-1] * (target + 1) for _ in range(n + 1)]
        def dfs(i, curSum):
            if i >= n or curSum > target:
                return False
            if curSum == target:
                return True 
            if memo[i][curSum] != -1:
                return memo[i][curSum]
            
            memo[i][curSum] = dfs(i + 1, curSum) or dfs(i + 1, curSum + nums[i])
            return memo[i][curSum]
        
        return dfs(0, 0)