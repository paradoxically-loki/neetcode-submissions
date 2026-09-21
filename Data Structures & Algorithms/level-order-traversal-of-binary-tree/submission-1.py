# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root: return res

        q = deque()
        q.append(root)

        while q:
            layer = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    layer.append(curr.val)
                if curr and curr.left: 
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
            res.append(layer)

        return res
        