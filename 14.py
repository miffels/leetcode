class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        min = sorted([len(s) for s in strs])[0]
        
        i = 1
        while i <= min and all([s.startswith(strs[0][:i]) for s in strs]):
            i += 1

        return strs[0][:i - 1]
        

solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix([]))
print(solution.longestCommonPrefix([""]))
print(solution.longestCommonPrefix(["", ""]))
