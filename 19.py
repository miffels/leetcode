from typing import Optional

from ListNode import ListNode, l

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        t = head
        p = head
        c = 1
        while t.next is not None:

            if c > n:
                p = p.next
            t = t.next
            c += 1
        
        if c == n:
            return head.next
        
        p.next = p.next.next
        
        return head


solution = Solution()

print(solution.removeNthFromEnd(l([1,2,3,4,5]), 2))
print(solution.removeNthFromEnd(l([1]), 1))
print(solution.removeNthFromEnd(l([1,2]), 1))
