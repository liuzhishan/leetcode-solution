# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        path = []
        res = []
        self.dfs(candidates, target, 0, path, res)

        return res

    def dfs(
        self,
        candidates: List[int],
        target: int,
        pos: int,
        path: List[int],
        res: List[List[int]],
    ) -> None:
        if target == 0:
            res.append([x for x in path])
            return

        for i in range(pos, len(candidates)):
            if candidates[i] > target:
                break

            path.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, path, res)
            path.pop()
