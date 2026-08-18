class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l, r = 0, 0
        length = 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                length += 1
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        
        return res