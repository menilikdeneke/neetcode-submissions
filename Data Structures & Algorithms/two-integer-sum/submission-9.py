class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            val = target - num
            if val in seen:
                if i < seen[val]:
                    return [i, seen[val]]
                else:
                    return [seen[val], i]
            else:
                seen[num] = i