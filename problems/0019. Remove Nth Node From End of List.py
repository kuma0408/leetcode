# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get list length
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        # get remove target index
        remove_idx = count - n

        current = head
        count = 0

        if remove_idx == 0:
            # if first node is remove node, then simply return seconde node
            return head.next

        while current:
            count += 1
            # skip next node if next node is remove node
            if count == remove_idx:
                current.next = current.next.next
                current = current.next
                return head
            else:
                current = current.next
        
        return head