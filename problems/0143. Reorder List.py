import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head2 = copy.copy(head)
        count = 0
        prev = None
        curr = head2

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        while count > 0:
            head_next = head.next
            head.next = head2
            head2_next = head2.next
            head2.next = head.next.next

