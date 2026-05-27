class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0

        while right < len(prices):
            maxP = max(maxP, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left += 1
            else:
                right += 1
        return maxP