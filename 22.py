class Solution:
    # Seems correct but rejected by LeetCode because order matters (wut?)
    def generateParenthesis(self, n: int, s = None) -> list[str]:
        res = ["()"]
        for i in range(1, n):
            temp = []
            for ri, r in enumerate(res):
                temp.append("()" + r)
                temp.append("(" + r + ")")
                if(ri > 0):
                    temp.append(r + "()")
            res = temp

        return res

        

solution = Solution()

print(solution.generateParenthesis(3))
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(4))
