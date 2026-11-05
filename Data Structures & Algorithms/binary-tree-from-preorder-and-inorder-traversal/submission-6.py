# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inoMap = {v : i for i, v in enumerate(inorder)}
        idx = 0

        def build(l, r):
            nonlocal idx
            if l > r:
                return None
            node = TreeNode(preorder[idx])
            idx += 1
            m = inoMap[node.val]
            node.left = build(l, m-1)
            node.right = build(m+1, r)
            return node

        return build(0, len(preorder) - 1)