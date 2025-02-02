# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)

        res = []
        path = []

        self.dfs(s, 0, n, path, res)

        return res
    
    def dfs(self, s: str, start: int, n: int, path: List[str], res: List[str]) -> None:
        if len(path) == 4:
            if start == n:
                res.append('.'.join(path))
            return

        for i in range(start, n):
            if s[start] == '0' and i > start:
                break

            if int(s[start: i + 1]) > 255:
                break

            path.append(s[start: i + 1])
            self.dfs(s, i + 1, n, path, res)
            path.pop()