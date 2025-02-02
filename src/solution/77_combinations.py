# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0:
            return []

        res = []
        path = []

        self.dfs(n, k, 1, path, res)

        return res

    def dfs(self, n: int, k: int, cur: int, path: List[int], res: List[List[int]]):
        if len(path) == k:
            res.append([x for x in path])
            return

        if cur > n:
            return

        path.append(cur)
        self.dfs(n, k, cur + 1, path, res)
        path.pop()
        self.dfs(n, k, cur + 1, path, res)
