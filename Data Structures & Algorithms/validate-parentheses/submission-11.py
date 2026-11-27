class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"]": "[", "}" : "{", "]" : "[", ")": "("}
        stack = []

        for c in s:
            if c not in open_to_close:
                stack.append(c)
            elif stack and stack[-1] == open_to_close[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return False if stack else True
