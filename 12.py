class Solution:
    def intToRoman(self, num: int) -> str:
        r = [(1000, "M"),
             (900, "CM"),
             (500, "D"),
             (400, "CD"),
             (100, "C"),
             (90, "XC"),
             (50, "L"),
             (40, "XL"),
             (10, "X"),
             (9, "IX"),
             (5, "V"),
             (4, "IV"),
             (1, "I")]
        res = ""
        i = 0
        while num > 0:
            while r[i][0] > num:
                i += 1
            d = num // r[i][0]
            res += d * r[i][1]
            num -= d * r[i][0]
        return res
        
solution = Solution()

print(solution.intToRoman(3749))
print(solution.intToRoman(58))
print(solution.intToRoman(1994))
