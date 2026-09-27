class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # cycle in a directed graph, topological sorting?

        adj = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses

        for src, dst in prerequisites: #main, prereq
            adj[dst].append(src) 
            inDegree[src] += 1

        q = deque()
        for idx, val in enumerate(inDegree):
            if val == 0:
                q.append(idx)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for neighbor in adj[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)

        return len(topo) == numCourses
