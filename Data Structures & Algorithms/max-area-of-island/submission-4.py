class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or visit[r][c]:
                return 0

            visit[r][c] = True

            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if not visit[r][c]:
                    res = max(res, dfs(r,c))
        return res
        