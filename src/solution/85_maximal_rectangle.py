# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        left = [[0 for i in range(m)] for j in range(n)]

        if matrix[0][0] == '1':
            left[0][0] = 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if j > 0:
                        left[i][j] = left[i][j - 1] + 1
                    else:
                        left[i][j] = 1

        max_area = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    max_area = max(max_area, left[i][j])
                    width = left[i][j]
                    for k in range(i - 1, -1, -1):
                        width = min(width, left[k][j])
                        max_area = max(max_area, width * (i - k + 1))

        return max_area
