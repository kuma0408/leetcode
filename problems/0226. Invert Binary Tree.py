# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def change(node):
            left = node.left
            right = node.right
            # exchange right and left node
            node.right = left
            node.left = right

            if node.left is not None:
                change(node.left)
            if node.right is not None:
                change(node.right)
            
            if node.left is None and node.right is None:
                return
            
        if root is None:
            return None

        change(root)
        return root
