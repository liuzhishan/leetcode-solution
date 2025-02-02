# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        n = len(grid)
        m = len(grid[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[n - 1][m - 1]