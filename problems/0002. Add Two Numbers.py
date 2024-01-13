# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_add = False
        dummy_head = ListNode(next=ListNode())
        curr = dummy_head
        while l1 or l2 or next_add:
            curr = curr.next
            val = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + (1 if next_add else 0)
            digit = val % 10
                
            # if val is over 10, add 1 to next val
            next_add = (digit != val)

            curr.val = digit
            curr.next = ListNode()

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        curr.next = None
        return dummy_head.next