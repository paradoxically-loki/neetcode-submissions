from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        rows = m
        cols = n

        @lru_cache(maxsize = None)
        def dfs(i, j):

            if i == rows-1 and j == cols-1:
                return 1

            if i >= rows or j >= cols:
                return 0

            return dfs(i,j+1) + dfs(i+1,j)

        return dfs(0,0)
        