# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self): 
        return "%d" % self.val + (self.next.__repr__() if self.next is not None else "")

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = []
        res = None
        carr = 0
        radix = 10
        while(l1 is not None or l2 is not None or carr > 0):
            # zero-padding if input lists are of different length
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            d = carr + v1 + v2
            sum.append(d % radix)
            carr = d // radix
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        

        for d in reversed(sum):
            res = ListNode(d, res)

        return res
    
solution = Solution()

def makeList(nums: list[int]) -> Optional[ListNode]:
    node = None
    for n in nums:
        node = ListNode(n, node)
    return node

# print(makeList([1, 2, 3]))
# print(solution.addTwoNumbers(makeList([3, 4, 2]), makeList([4, 6, 5])))
print(solution.addTwoNumbers(makeList([9,9,9,9,9,9,9]), makeList([9,9,9,9])))