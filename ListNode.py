# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "%d" % self.val + (self.next.__repr__() if self.next is not None else "")

def l(items) -> Optional[ListNode]:
    n = None
    for i in reversed(items):
        n = ListNode(i, n)
    return n
