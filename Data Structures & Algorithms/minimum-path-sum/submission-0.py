class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        memo = {}

        def dfs(r,c):
            if (r,c) == (n-1,m-1):
                return grid[n-1][m-1]

            if r>=n or c>=m:
                return float('inf')

            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = grid[r][c] + min(dfs(r+1,c), dfs(r,c+1))
            return memo[(r,c)]
        
        return dfs(0,0)