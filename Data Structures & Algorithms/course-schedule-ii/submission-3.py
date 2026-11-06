class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        topo = []

        while q:
            c = q.popleft()
            topo.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return topo if len(topo) == numCourses else []