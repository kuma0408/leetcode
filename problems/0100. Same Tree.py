# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if p == q:
                # both p and q are None
                return True
            else:
                return False
            
        ret = True

        def dfs(node1, node2):
            nonlocal ret
            if node1 is None or node2 is None:
                if node1 != node2:
                    ret = False
                return

            if node1.val != node2.val:
                ret = False
                return

            node1_left = node1.left
            node2_left = node2.left
            dfs(node1_left, node2_left)

            node1_right = node1.right
            node2_right = node2.right
            dfs(node1_right, node2_right)

        dfs(p, q)
        return ret
