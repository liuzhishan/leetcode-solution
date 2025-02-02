# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        path = []
        visited = [False for _ in range(len(nums))]

        res = []

        self.dfs(nums, 0, path, visited, res)

        return res

    def dfs(self, nums: List[int], start: int, path: List[int], visited: List[bool], res: List[List[int]]) -> None:
        res.append([x for x in path])

        for i in range(start, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            path.append(nums[i])
            visited[i] = True
            self.dfs(nums, i + 1, path, visited, res)
            path.pop()
            visited[i] = False