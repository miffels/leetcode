class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        chars: dict[str, int] = {}
        max = len(s) if len(s) < 2 else 0
        while(r < len(s)):
            lc = s[l]
            rc = s[r]
            chars[lc] = l
            if rc in chars:
                l = chars[rc] + 1
                chars = {k:v for k, v in chars.items() if v >= l}
            chars[rc] = r
            r += 1
            i = len(chars)
            max = i if i > max else max
        return max
        
solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))    #3
print(solution.lengthOfLongestSubstring("bbbbb"))       #1
print(solution.lengthOfLongestSubstring(" "))           #1
print(solution.lengthOfLongestSubstring("ohvhjdml"))    #6
print(solution.lengthOfLongestSubstring("wobgrovw"))    #6
print(solution.lengthOfLongestSubstring("pwwkekw"))     #3