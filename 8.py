class Solution:
    def myAtoi(self, s: str) -> int:
        # guard - empty string & whitespace
        s = s.strip()
        if(not s):
            return 0
        
        # calculate and remove sign
        sgn = -1 if s[0] == "-" else 1
        if(sgn < 0) or s[0] == "+":
            s = s[1:]
        
        # iterate digits
        digits="0123456789"
        res = 0
        for c in s:
            if not c in digits:
                break
            res = res * 10 + int(c)

        # reapply sign
        res *= sgn

        # clipping
        if res > 2**31-1:
            res = 2**31-1
        if res < -2**31:
            res = -2**31
        
        return res
    
solution = Solution()

print(solution.myAtoi("42"))
print(solution.myAtoi("  -42"))
print(solution.myAtoi("1337c0d3"))
print(solution.myAtoi("0-1"))
print(solution.myAtoi("+1"))
