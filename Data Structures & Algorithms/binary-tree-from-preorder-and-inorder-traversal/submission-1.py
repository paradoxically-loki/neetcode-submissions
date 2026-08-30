# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index = {val:i for i, val in enumerate(inorder)}
        self_preorder_idx = 0

        def helper(left, right):
            nonlocal self_preorder_idx

            if left > right:
                return

            root_val = preorder[self_preorder_idx]
            root = TreeNode(root_val)
            self_preorder_idx += 1


            mid = inorder_index[root_val]

            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root

        return helper(0, len(preorder)-1) 
        