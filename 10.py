import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Seriously, if regex exists, don't reinvent it.
        p = re.sub("\\*+", "*", "^%s$" % p)
        return re.match(p, s) is not None
    
solution = Solution()

print(solution.isMatch("aa", "a"))
print(solution.isMatch("aa", "a*"))
print(solution.isMatch("ab", ".*"))
print(solution.isMatch("aab", "c*a*b"))
print(solution.isMatch("mississippi", "mis*is*ip*."))