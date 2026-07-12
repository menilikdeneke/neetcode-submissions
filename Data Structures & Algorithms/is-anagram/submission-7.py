class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = Counter(s)
        second = Counter(t)

        return first == second