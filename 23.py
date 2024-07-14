from typing import Optional

from ListNode import ListNode, l


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = []
        while any(n is not None for n in lists):
            min = None
            argmin = None

            for i, li in enumerate(lists):
                if li is None:
                    continue
                if min is None or li.val < min:
                    argmin = i
                    min = li.val

            if argmin is not None:
                res.append(min)
                if lists[argmin] is not None:
                    lists[argmin] = lists[argmin].next
            lists = [n for n in lists if n is not None]
        
        return l(res)
        
solution = Solution()

print(solution.mergeKLists([l(i) for i in [[1,4,5],[1,3,4],[2,6]]]))
print(solution.mergeKLists([l(i) for i in []]))
print(solution.mergeKLists([l(i) for i in [[]]]))
