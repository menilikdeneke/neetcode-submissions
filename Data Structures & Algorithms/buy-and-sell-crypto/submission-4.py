class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            while prices[r] < prices[l]:
                l += 1
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
            r += 1
        
        return maxP