# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        dp[0][0] = True

        for i in range(n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    if j - 2 >= 0:
                     dp[i][j] |= dp[i][j - 2]
                    if i - 1 >= 0 and j - 2 >= 0 and p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                    elif i - 1 >= 0 and j - 2 >= 0 and p[j - 2] != '.':
                        dp[i][j] |= dp[i - 1][j] and s[i - 1] == p[j - 2]
                    else:
                        pass
                else:
                    if i - 1 >= 0 and j - 1 >= 0:
                        dp[i][j] |= dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                    elif i - 1 >= 0:
                        dp[i][j] |= dp[i - 1][j]
                    else:
                        pass

        return dp[n][m]

