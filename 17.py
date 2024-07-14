class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) < 1:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = list(letters[digits[0]])

        for d in digits[1:]:
            temp = []
            for r in res:
                for l in letters[d]:
                    temp.append(r + l)
            res = temp

        return res
        
solution = Solution()

print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
print(solution.letterCombinations("2"))
