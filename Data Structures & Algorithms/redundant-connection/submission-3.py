class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # search for cycle and remove the edge that makes us the cycle
        # 
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque(i for i in indegree.keys() if indegree[i] == 1)
        
        seen = set()
        while q:
            node = q.popleft()
            seen.add(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v] == 2:
                return [u, v]
