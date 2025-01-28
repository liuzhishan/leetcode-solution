# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.run(res, "", 0, 0, n)

        return res

    def run(self, res: List[str], s: str, left: int, right: int, n: int):
        if len(s) == n * 2:
            res.append(s)
            return
        
        if left < n:
            self.run(res, s + "(", left + 1, right, n)
        if right < left:
            self.run(res, s + ")", left, right + 1, n)