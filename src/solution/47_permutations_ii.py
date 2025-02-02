# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = [False for _ in range(len(nums))]
        path = []
        res = []

        nums.sort()
        self.run(nums, path, visited, res)

        return res
    
    def run(self, nums: List[int], path: List[int], visited: List[bool], res: List[List[int]]):
        if len(path) == len(nums):
            res.append([x for x in path])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            path.append(nums[i])
            visited[i] = True
            self.run(nums, path, visited, res)
            path.pop()
            visited[i] = False
