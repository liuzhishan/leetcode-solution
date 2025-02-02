# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return

        m = len(matrix[0])

        zero_cols = []
        for i in range(n):
            has_zero = False
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_cols.append(j)
                    has_zero = True

            if has_zero:
                for j in range(m):
                    matrix[i][j] = 0

        for col in zero_cols:
            for i in range(n):
                matrix[i][col] = 0