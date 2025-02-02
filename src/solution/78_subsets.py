# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()

        n = len(nums)
        res = []
        path = [False for _ in range(n)]

        self.dfs(nums, n, 0, path, res)

        return res

    def dfs(self, nums: List[int], n: int, pos: int, path: List[int], res: List[List[int]]):
        if pos == n:
            res.append([nums[i] for i in range(n) if path[i] == True])
            return

        path[pos] = True
        self.dfs(nums, n, pos + 1, path, res)
        path[pos] = False
        self.dfs(nums, n, pos + 1, path, res)
