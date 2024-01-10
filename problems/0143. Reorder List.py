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
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        # set first half period and reverse second half period
        prev = slow.next = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        # merge two halfs
        first, second = head, prev
        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first = next1
            second = next2