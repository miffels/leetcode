from typing import Optional

from ListNode import ListNode, l

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while list1 is not None or list2 is not None:
            if list1 is None:
                temp.append(list2.val)
                list2 = list2.next
            elif list2 is None:
                temp.append(list1.val)
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    temp.append(list1.val)
                    list1 = list1.next
                else:
                    temp.append(list2.val)
                    list2 = list2.next
            
        return l(temp)

solution = Solution()

print(solution.mergeTwoLists(l([1,2,4]), l([1,3,4])))
print(solution.mergeTwoLists(l([]), l([])))
print(solution.mergeTwoLists(l([]), l([0])))
