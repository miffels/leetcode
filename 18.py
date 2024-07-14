class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums) < 4:
            return []
        nums.sort()

        res = []

        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d+1]:
                            d -=1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                    elif s > target:
                        d -= 1
                    else:
                        c += 1

        return res
        

solution = Solution()

print(solution.fourSum([1,0,-1,0,-2,2], 0))
print(solution.fourSum([2,2,2,2,2], 8))
print(solution.fourSum([-3,-2,-1,0,0,1,2,3], 0))
