from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0]* cols for _ in range(rows)]

        dp[0][0] = grid[0][0]

        # first row
        for i in range(1, cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        # first col
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # remaining
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        return dp[rows-1][cols-1]