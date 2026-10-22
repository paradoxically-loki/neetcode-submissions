class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        def dfs(r, c):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            currArea = 0
            for dr, dc in directions:
                currArea += dfs(r+dr, c+dc)
            
            return 1 + currArea

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea


        