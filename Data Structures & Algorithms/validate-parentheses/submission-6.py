class Solution:
    def isValid(self, s: str) -> bool:
        matches = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            if c in matches:
                if stack and stack[-1] == matches[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False