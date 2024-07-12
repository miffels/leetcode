class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        # print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            t = -nums[i]
            l = i + 1
            r = len(nums) - 1
            
            while l < r:

                s = nums[l] + nums[r]

                # print(i, l, r, "\t", t, s)

                if t == s:
                    res.append([nums[i], nums[l], nums[r]])

                    while nums[r] == nums[r-1] and l < r - 1:
                        r -= 1
                    while nums[l] == nums[l+1] and l < r - 1:
                        l += 1

                    l += 1
                    r -= 1
                elif s > t:
                    r -= 1
                else:
                    l += 1

        return res
        
solution = Solution()

print(solution.threeSum([0,1,1]))
print(solution.threeSum([0, 0, 0]))
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum([0,0,0,0]))
print(solution.threeSum([-2,0,1,1,2]))
print(solution.threeSum([1,-1,-1,0]))
