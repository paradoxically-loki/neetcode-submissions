class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites: # b -> a
            adj[b].append(a)
            indegree[a] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0

        while q:
            c = q.popleft()
            taken += 1
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return taken == numCourses


        