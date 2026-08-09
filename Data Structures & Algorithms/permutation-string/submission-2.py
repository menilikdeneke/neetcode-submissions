class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCounter1 = Counter(s1)
        charCounter2 = Counter()

        l = 0

        for r in range(len(s2)):
            charCounter2[s2[r]] += 1
            if (r - l) + 1 > len(s1):
                charCounter2[s2[l]] -= 1
                if charCounter2[s2[l]] == 0:
                    del charCounter2[s2[l]]
                l += 1
            
            if charCounter1 == charCounter2:
                return True
        return False