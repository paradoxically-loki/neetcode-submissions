class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2: q.append((r, c))
                elif grid[r][c] == 1: fresh += 1

        count = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                    if (0 <= nr < R) and (0 <= nc < C) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            count += 1

        return count if fresh == 0 else -1
        