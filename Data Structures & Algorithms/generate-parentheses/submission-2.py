class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(op, close):
            if close == op == n:
                res.append("".join(stack))
                return
            
            if op < n:
                stack.append("(")
                dfs(op + 1, close)
                stack.pop()
            if close < op:
                stack.append(")")
                dfs(op, close + 1)
                stack.pop()
            
            return res
        
        dfs(0, 0)
        return res