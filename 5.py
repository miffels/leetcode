class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def palindrome(i, j):
            m = (i+j)//2
            l = i
            r = j
            while l < m and r > m:
                if s[l] != s[r - 1]:
                    return ""
                l += 1
                r -= 1
            return s[i:j]
        
        res = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if(j-i > len(res)):
                    p = palindrome(i, j)
                    res = p if len(p) > len(res) else res
        return res
    
solution = Solution()

print(solution.longestPalindrome("bab"))
print(solution.longestPalindrome("def"))
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome(""))
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("bb"))
