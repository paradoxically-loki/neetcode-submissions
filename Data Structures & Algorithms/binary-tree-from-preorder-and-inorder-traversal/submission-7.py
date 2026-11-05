# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inoMap = {v : i for i, v in enumerate(inorder)}
        pre = iter(preorder)

        def build(l, r):
            if l > r:
                return None
            node = TreeNode(next(pre))
            m = inoMap[node.val]
            node.left = build(l, m-1)
            node.right = build(m+1, r)
            return node

        return build(0, len(preorder) - 1)