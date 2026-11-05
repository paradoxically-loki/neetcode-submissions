class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, seen, prevVal):
            if (r, c) in seen or not (0 <= r < R and 0 <= c < C) or heights[r][c] < prevVal:
                return

            seen.add((r, c))
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                dfs(nr, nc, seen, heights[r][c])

        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C-1, atl, heights[r][C-1])

        for c in range(C):
            dfs(0, c, pac, heights[0][c])
            dfs(R-1, c, atl, heights[R-1][c])

        return [list(p) for p in pac & atl]


        