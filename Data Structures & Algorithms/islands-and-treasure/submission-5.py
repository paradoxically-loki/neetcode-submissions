class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        R, C = len(grid), len(grid[0])
        INF = 2147483647

        q = deque((r,c) for r in range(R) for c in range(C) if grid[r][c] == 0)

        while q:
            r, c = q.popleft()
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))


