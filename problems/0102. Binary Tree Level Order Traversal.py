# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        
        def bfs(root, level):
            nonlocal ret
            if root is None:
                return
            
            if len(ret) <= level:
                ret.append([])

            ret[level].append(root.val)
            level += 1

            bfs(root.left, level)
            bfs(root.right, level)

        bfs(root, 0)
        return ret
