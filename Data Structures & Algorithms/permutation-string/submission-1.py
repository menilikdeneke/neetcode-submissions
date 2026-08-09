class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charCounter1 = Counter(s1)
        charCounter2 = {}

        l, r = 0, 0
        
        for r in range(len(s2)):
            # Add right character to current window
            charCounter2[s2[r]] = 1 + charCounter2.get(s2[r], 0)

            # Keep window size equal to len(s1)
            if (r - l + 1) > len(s1):
                charCounter2[s2[l]] -= 1
                if charCounter2[s2[l]] == 0:
                    del charCounter2[s2[l]]  # Clean up zero counts
                l += 1
            if charCounter1 == charCounter2:
                return True
            r += 1

        return False