class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            

        def dfs(node, parent):
            height = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                height = max(height, 1 + dfs(nei, node))
            return height

        minHeight = n
        res = []
        for i in range(n):
            currHeight = dfs(i,-1)
            if currHeight == minHeight:
                res.append(i)
            elif currHeight < minHeight:
                res = [i]
                minHeight = currHeight
        return res
