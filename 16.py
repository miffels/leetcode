class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        res = float('-inf')

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if(abs(target - s) < abs(target - res)):
                    res = s

                if target == res:
                    return res
                elif s > target:
                    r -= 1
                else:
                    l += 1

        return res

solution = Solution()

print(solution.threeSumClosest([0,0,0], 1))
print(solution.threeSumClosest([-1,2,1,-4], 1))
print(solution.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
