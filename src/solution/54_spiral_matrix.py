# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        res = []

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        dir_x, dir_y = 0, 1
        x, y = 0, 0

        for i in range(n * m):
            res.append(matrix[x][y])

            x, y = x + dir_x, y + dir_y

            if y > right:
                y = right
                x += 1
                dir_x, dir_y = 1, 0
                top += 1
            elif x > bottom:
                x = bottom
                y -= 1
                dir_x, dir_y = 0, -1
                right -= 1
            elif y < left:
                y = left
                x -= 1
                dir_x, dir_y = -1, 0
                bottom -= 1
            elif x < top:
                x = top
                y += 1
                dir_x, dir_y = 0, 1
                left += 1

        return res