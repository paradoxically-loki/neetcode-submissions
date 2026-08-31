class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c, res = len(grid), len(grid[0]), 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    res += (i+1 >= r or grid[i+1][j] == 0)
                    res += (j+1 >= c or grid[i][j+1] == 0)
                    res += (i-1 < 0 or grid[i-1][j] == 0)
                    res += (j-1 < 0 or grid[i][j-1] == 0)
        return res
        