class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(a, b):
            if a == 0:
                return 0
            if b == 0:
                return 1
            
            res = helper(a, b // 2)
            res = res * res
            return a * res if b % 2 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res