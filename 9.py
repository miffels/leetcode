class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        if len(s) == 1:
            return True
        
        mid = (len(s) + 1) // 2

        i = 0
        j = len(s) - 1
        res = True
        while i < mid:
            if s[i] != s[j]:
                res = False
                break
            i += 1
            j -= 1
        return res
        
solution = Solution()

print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
