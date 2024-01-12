# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        d = {}
        curr = head
        while curr:
            d[curr] = Node(x=curr.val)
            curr = curr.next

        curr = head
        while curr:
            # use get() method in case Node is None
            d[curr].next = d.get(curr.next)
            d[curr].random = d.get(curr.random)
            curr = curr.next

        return d[head]