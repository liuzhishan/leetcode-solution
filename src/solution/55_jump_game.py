# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        n = len(nums)
        max_dist = 0

        for i in range(n):
            if max_dist < i:
                return False

            max_dist = max(max_dist, i + nums[i])

            if max_dist >= n - 1:
                return True

        return False