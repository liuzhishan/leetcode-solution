# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0 for _ in range(2 ** n)]

        for i in range(2 ** n):
            res[i] = (i >> 1) ^ i

        return res
