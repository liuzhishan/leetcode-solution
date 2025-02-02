# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            s = mid * mid

            if s == x:
                return mid
            elif s > x:
                right = mid - 1
            else:
                left = mid + 1

        return right