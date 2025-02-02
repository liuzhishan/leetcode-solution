# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        res = 0
        for i in range(n - 1, -1, -1):
            if s[i] != ' ':
                res += 1
            elif res > 0:
                break

        return res