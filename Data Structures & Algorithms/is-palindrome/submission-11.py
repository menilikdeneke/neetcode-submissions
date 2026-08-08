class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True


    def isAlphaNum(self, s):
        l, r = 0, len(s) - 1

        return ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z') or ord('0') <= ord(s) <= ord('9')