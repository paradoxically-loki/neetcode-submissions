# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def arm(node):
            nonlocal best

            if not node:
                return 0
                
            l = max(arm(node.left), 0)
            r = max(arm(node.right), 0)

            best = max(best, node.val + l + r)

            return node.val + max(l,r)

        arm(root)
        return best

