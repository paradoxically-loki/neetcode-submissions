class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque((r,c) for r in range(R) for c in range(C) if grid[r][c] == 2)

        count = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                    if (0 <= nr < R) and (0 <= nc < C) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            count +=1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
        return max(0, count - 1)

        