# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        n = len(s1)
        d = [[[False for i in range(n + 1)] for j in range(n)] for k in range(n)]

        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    d[i][j][1] = True

        for k in range(2, n + 1):
            for i in range(n):
                for j in range(n):
                    for m in range(1, k):
                        if i + m < n and j + m < n and d[i][j][m] and d[i + m][j + m][k - m]:
                            d[i][j][k] = True
                        elif i + m < n and j + k - m < n and d[i][j + k - m][m] and d[i + m][j][k - m]:
                            d[i][j][k] = True
                        else:
                            pass

        return d[0][0][n]