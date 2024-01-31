# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = True

        def bfs(root):
            nonlocal ret
            if root is None:
                return
            
            if root.left:
                if root.left.val < root.val:
                    bfs(root.left)
                else:
                    ret = False
                    return

            if root.right:
                if root.right.val > root.val:
                    bfs(root.right)
                else:
                    ret = False
                    return
        
        bfs(root)
        return ret