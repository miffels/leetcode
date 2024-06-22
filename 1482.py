class Solution:

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if(m*k > len(bloomDay)):
            return -1
        l = min(bloomDay)
        r = max (bloomDay)
        day = (l + r) // 2
        while l < r:
            seq = 0
            c = 0
            for d in bloomDay:
                if d <= day:
                    seq += 1
                    if(seq % k == 0):
                        c += 1
                else:
                    seq = 0
                seq %= k
                if(c == m):
                    break

            if(c >= m):
                r = day
            else:
                l = day + 1
            day = (l + r) // 2
        return day
    
solution = Solution()

print(solution.minDays([81,23,10,90,68,43,81,10,92,65,47,57,51,74,61,79,18,52,74,90], 2, 7))
print(solution.minDays([1000000000,1000000000], 1, 1))
