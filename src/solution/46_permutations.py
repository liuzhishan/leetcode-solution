# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        self.run(nums, 0, path, res)
        
        return res

    def run(self, nums: List[int], cur: int, path: List[int], res: List[List[int]]):
        if cur == len(nums):
            res.append([x for x in path])
            return
        
        for i in range(len(nums)):
            if nums[i] in path:
                continue

            path.append(nums[i])
            self.run(nums, cur + 1, path, res)
            path.pop()