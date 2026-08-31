class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 0
            
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                if r+dr < rows and c+dc < cols and grid[r+dr][c+dc]:
                    area += dfs(r+dr, c+dc)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    out = dfs(r,c)
                    max_area = max(max_area, out)

        return max_area

        