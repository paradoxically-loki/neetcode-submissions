class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # let's try the dfs approach to detect cycle

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False]*n

        def dfs(node, parent):
            visit[node] = True
            for neighbor in adj[node]:
                if not visit[neighbor]:
                    if dfs(neighbor, node):
                        return True

                elif neighbor != parent:
                    return True

            return False

        count = 0
        for i in range(n):
            if not visit[i]:
                count += 1
                if dfs(i,-1) or count > 1:
                    return False

        return True