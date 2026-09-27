class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cycle detection in a directed graph, dfs 
        adj = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)

        visit = [False]*numCourses
        pathVisit = [False]*numCourses

        def dfs(node):
            visit[node] = True
            pathVisit[node] = True

            for neighbor in adj[node]:
                if not visit[neighbor]:
                    if dfs(neighbor): 
                        return True
                elif pathVisit[neighbor]:
                    return True

            pathVisit[node] = False
            return False

        for i in range(numCourses):
            if not visit[i]:
                if dfs(i): # cycle found, can't finish
                    return False
        return True
        