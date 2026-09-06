class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        memo = {}

        def dfs(r,c):
            if (r,c) == (n-1,m-1):
                return 1

            if r < 0 or c < 0 or r >= n or c >= m or obstacleGrid[r][c] == 1:
                return 0

            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return memo[(r,c)]
        
        return dfs(0,0)
        