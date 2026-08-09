class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        res = 0
        length = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            length += 1
            maximum = max(count.values())

            while (sum(count.values()) - maximum) > k:
                if count[s[l]] >= 1:
                    count[s[l]] -= 1
                length -= 1
                l += 1
            res = max(length, res)
            r += 1
        
        return res

            