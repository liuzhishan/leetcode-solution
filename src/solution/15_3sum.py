# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        for i in range(n):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            k = n - 1

            for j in range(i + 1, n):
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:
                    continue

                while j < k and nums[j] + nums[k] > target:
                    k -= 1

                if j == k:
                    break

                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])

        return res
