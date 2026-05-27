class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')':'(', ']':'[', '}':'{'}
        stack = []
        if len(s) < 2:
            return False
        else:
            for ch in s:
                if ch not in parentheses.keys() and ch not in parentheses.values():
                    return False
                elif ch not in parentheses:
                    stack.append(ch)
                elif ch in parentheses:
                    if len(stack) == 0:
                        return False
                    elif parentheses[ch] == stack[len(stack) - 1]:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0