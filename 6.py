class Solution:
    def convert(self, s: str, numRows: int) -> str:
        chars: list[str] = []
        idxs = []
        t = (numRows-1)*2 if numRows > 1 else 1
        # Poorly optimized attempt at approaching something like a
        # mapping function as opposed to a generative zig-zag motion
        for r in range(numRows):
            o = (numRows - r - 1)*2
            for c in range(0, len(s), t):
                if(c+r) < len(s):
                    chars.append(s[c+r])
                    idxs.append("%d" % (c+r))
                if(o < t and o > 1 and c+r+o < len(s)):
                    chars.append(s[c+r+o])
                    idxs.append("%d" % (c+r+o))
        return "".join(chars)
    
solution = Solution()

print(solution.convert("PAYPALISHIRING", 3))    # PAHNAPLSIIGYIR
print(solution.convert("PAYPALISHIRING", 4))    # PINALSIGYAHRPI
print(solution.convert("A", 1))                 # A
print(solution.convert("AB", 2))                # AB
