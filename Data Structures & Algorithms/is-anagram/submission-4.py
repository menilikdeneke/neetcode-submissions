class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firsth = {}
        secondh = {}

        for ch in s:
            if ch in firsth:
                firsth[ch] += 1
            else:
                firsth[ch] = 1
        
        for ch in t:
            if ch in secondh:
                secondh[ch] += 1
            else:
                secondh[ch] = 1
        
        if firsth == secondh :
            return True
        return False