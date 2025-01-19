# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        for i in range(n):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:
                    continue

                h = n - 1
                for k in range(j + 1, n):
                    if k - 1 >= j + 1 and nums[k] == nums[k - 1]:
                        continue

                    while h > k and nums[h] + nums[k] + nums[j] + nums[i] > target:
                        h -= 1
                    
                    if k >= h:
                        break

                    v = nums[i] + nums[j] + nums[k] + nums[h]
                    if v == target:
                        res.append([nums[i], nums[j], nums[k], nums[h]])

        return res
