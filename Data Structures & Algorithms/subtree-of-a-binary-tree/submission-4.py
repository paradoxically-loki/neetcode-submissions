# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot: return True

        if not root: return False

        if self.identical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def identical(self, root, subRoot):
        if not root or not subRoot: return root == subRoot

        if root.val != subRoot.val:
            return False

        return self.identical(root.left, subRoot.left) and self.identical(root.right, subRoot.right)
        