class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])

        dp = [float('inf')]*(m+1)
        dp[m-1] = 0

        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                dp[c] = grid[r][c] + min(dp[c], dp[c+1])

        return dp[0]
        