class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        closing = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        cp = 0
        cb = 0
        cc = 0
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif len(stack) > 0 and stack[-1] == closing[c]:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
        
solution = Solution()

print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([)]"))
