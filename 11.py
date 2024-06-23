class Solution:
    def maxArea(self, height: list[int]) -> int:
        def argmin(i, j):
            return i if height[i] < height[j] else j
        def min(i, j):
            return height[argmin(i, j)]
        def area(i, j):
            return (j - i) * min(i, j)
        
        res = 0
        i = 0
        j = len(height) - 1
        while(i < j):
            a = area(i, j)
            res = a if a > res else res
            if i == argmin(i, j):
                i += 1
            else:
                j -= 1

        return res
    
solution = Solution()

print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))
