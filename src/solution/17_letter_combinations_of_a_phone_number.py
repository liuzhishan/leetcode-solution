# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        arr = ['' for _ in range(len(digits))]

        self.dfs(digits, 0, d, arr, res)

        return res

    def dfs(self, digits: str, pos: int, d: dict, arr: List[str], res: List[str]):
        if pos == len(digits):
            if len(arr) > 0:
                res.append(''.join(arr))
            return

        for x in d[digits[pos]]:
            arr[pos] = x
            self.dfs(digits, pos + 1, d, arr, res)
