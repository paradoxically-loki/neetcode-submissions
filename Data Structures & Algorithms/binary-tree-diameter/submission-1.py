# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(root):
            if not root: return 0

            leftHt = height(root.left)
            rightHt = height(root.right)

            self.max_diameter = max(self.max_diameter, leftHt+rightHt)

            return 1 + max(leftHt, rightHt)

        height(root)
        return self.max_diameter
        

        