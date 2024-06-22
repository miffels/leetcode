from typing import Optional


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> Optional[float]:
        n1 = len(nums1)
        n2 = len(nums2)

        if(n1 > n2):
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        l = 0
        r = len(nums1)

        while l <= r:
            p1 = (l + r) // 2
            p2 = (n + 1) // 2 - p1

            mxl1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            mxl2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            mnr1 = float('inf') if p1 == n1 else nums1[p1]
            mnr2 = float('inf') if p2 == n2 else nums2[p2]

            if(mxl1 <= mnr2 and mxl2 <= mnr1):
                return max(mxl1, mxl2) if n % 2 == 1 else (max(mxl1, mxl2) + min(mnr1, mnr2)) / 2
            elif(mxl1 > mnr2):
                r = p1 - 1
            else:
                l = p1 + 1

solution = Solution()

print(solution.findMedianSortedArrays([1, 3], [2]))
print(solution.findMedianSortedArrays([1, 2], [3, 4]))