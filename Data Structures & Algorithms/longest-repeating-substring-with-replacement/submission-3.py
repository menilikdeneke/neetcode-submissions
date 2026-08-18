class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        res = 0
        length = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            length += 1
            while sum(count.values()) - max(count.values()) > k:
                count[s[l]] -= 1
                length -= 1
                l += 1
        
            res = max(res, length)
            r += 1
        
        return res