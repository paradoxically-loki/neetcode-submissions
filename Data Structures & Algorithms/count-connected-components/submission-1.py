class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visit  = [False]*n

        def dfs(node):
            visit[node] = True
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if not visit[i]:
                dfs(i)
                count += 1

        return count
        