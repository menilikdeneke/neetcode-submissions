class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights) - 1

        while j > i:
            area = min(heights[i], heights[j]) * (j - i)
            res = max(area, res)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1       
        return res