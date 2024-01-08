# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2 if list2 is not None else None
        elif list2 is None:
            return list1 if list1 is not None else None
        
        # list1 always has first minimum num. 
        if list2.val <= list1.val:
            list1, list2 = list2, list1

        ret = list1
        ret_head = ret
        l1_head = list1.next
        l2_head = list2

        while l1_head is not None or l2_head is not None:
            # if either l1 or l2 is None, then the rest of the other list is simply added to ret list.
            if l2_head is None:
                ret_head.next = l1_head
                return ret
            elif l1_head is None:
                ret_head.next = l2_head
                return ret

            if l1_head.val <= l2_head.val:
                ret_head.next = l1_head
                l1_head = l1_head.next
                ret_head = ret_head.next
            else:
                ret_head.next = l2_head
                l2_head = l2_head.next
                ret_head = ret_head.next

        return ret