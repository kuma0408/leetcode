# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dig(node, current_depth):
            if node is None:
                return

            current_depth += 1
            self.max_depth = max(self.max_depth, current_depth)

            dig(node.left, current_depth)
            dig(node.right, current_depth)

        dig(root, 0)
        return self.max_depth