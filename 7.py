class Solution:
    def reverse(self, x: int) -> int:
        sgn = -1 if x < 0 else 1
        x *= sgn
        
        res: int = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        
        return 0 if res < -2**31 or res > 2**31-1 else sgn*res

solution = Solution()

print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
print(solution.reverse(0))