# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while True:
            if fast.next is None or fast.next.next is None:
                return False
            if slow is fast or slow is fast.next:
                return True
            else:
                slow = slow.next
                fast = fast.next.next