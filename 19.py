from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%d" % self.val + (self.next.__repr__() if self.next is not None else "")

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

def l(items) -> ListNode:
    n = None
    for i in reversed(items):
        n = ListNode(i, n)
    return n

print(solution.removeNthFromEnd(l([1,2,3,4,5]), 2))
print(solution.removeNthFromEnd(l([1]), 1))
print(solution.removeNthFromEnd(l([1,2]), 1))
