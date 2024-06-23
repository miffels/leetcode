class Solution:
    def romanToInt(self, s: str) -> int:
        rs = {
            "M" : 1000,
            "D" : 500,
            "C" : 100,
            "L" : 50,
            "X" : 10,
            "V" : 5,
            "I" : 1
        }
        res = 0
        for c1, c2 in zip(s, s[1:]):
            if rs[c1] < rs[c2]:
                res -= rs[c1]
            else:
                res += rs[c1]
        
        res += rs[s[-1]]
        return res
    
solution = Solution()

print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))