class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}

        for c in s:
            first[c] = first.get(c, 0) + 1
        
        for c in t:
            second[c] = second.get(c, 0) + 1
        
        return first == second