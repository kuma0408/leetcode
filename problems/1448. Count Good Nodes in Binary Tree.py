# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        max_val = root.val

        def bfs(root, max_val):
            nonlocal ret

            if root is None:
                return

            if max_val <= root.val:
                ret += 1
                bfs(root.right, root.val)
                bfs(root.left, root.val)
            else:
                bfs(root.right, max_val)
                bfs(root.left, max_val)
            
        bfs(root, max_val)
        return ret