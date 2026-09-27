class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # cycle detection in undirected graph?
        # also if all the graph is one component

        # let's try bfs?
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False]*n
        q = deque()

        def bfs(start):
            visit[start] = True
            q.append((start, -1))

            while q:
                node, parent = q.popleft()
                visit[node] = True
                for neighbor in adj[node]:
                    if not visit[neighbor]:
                        q.append((neighbor, node))
                    elif neighbor != parent:
                        return True # cycle detected

            return False # no cycle

        
        count = 0
        for i in range(n):
            if not visit[i]:
                count += 1
                if bfs(i) or count > 1: # if cycle or disconnected
                    return False

        return True
                    
