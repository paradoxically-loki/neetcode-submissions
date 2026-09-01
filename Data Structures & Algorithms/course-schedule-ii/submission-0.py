class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visit, curr = set(), set()

        def dfs(crs):
            if crs in curr:
                return False # cycle detected
            if crs in visit:
                return True # already processed, it was fine
            
            curr.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            curr.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
        