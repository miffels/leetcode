from typing import Optional


class Solution:

    def twoSum(self, nums: list[int], target: int) -> Optional[list[int]]:
        # build index
        table: dict[int, list[int]] = {}
        for i, n in enumerate(nums):
            if(n in table):
                table[n].append(i)
            else:
                table[n] = [i]


        # binary search for highest number < target
        sortedNums = sorted(nums)
        l = 0
        r = len(sortedNums) - 1
        mid = (l + r) // 2

        while l < r:
            if(sortedNums[mid] > (target - sortedNums[0])): # cut off values too big
                r = mid
            else:
                l = mid + 1
            mid = (l + r) // 2

        i = mid
        while i >= 0:
            n = sortedNums[i]
            j = table[n]
            if((target - n) in table):
                if(len(table[target - n]) == 2):
                    # special case: n = target/2
                    return table[target - n]
                return [table[target - n][0], j[0]]
            i -= 1

        return None

solution = Solution()

print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,3], 6))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([-2489365,-993808,-2556360], -3483173))
