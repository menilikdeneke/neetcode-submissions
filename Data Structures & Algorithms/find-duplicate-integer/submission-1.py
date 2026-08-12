class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while fast < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                new_slow = 0
                while slow < len(nums) and new_slow != slow:
                    new_slow = nums[new_slow]
                    slow = nums[slow]
                return slow