# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        max_pos = 0
        steps = 0

        for i in range(n - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                end = max_pos
                steps += 1

        return steps