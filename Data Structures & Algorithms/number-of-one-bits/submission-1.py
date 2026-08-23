class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = 1 << i
            if n & bit > 0:
                res += 1
        
        return res