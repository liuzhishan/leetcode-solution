# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                while j - 1 >= i + 1 and j < k and nums[j] == nums[j - 1]:
                    j += 1

                while j < k and k + 1 < n and nums[k] == nums[k + 1]:
                    k -= 1

                cur = nums[i] + nums[j] + nums[k]
                if abs(cur - target) < abs(closest - target):
                    closest = cur

                if cur < target:
                    j += 1
                elif cur > target:
                    k -= 1
                else:
                    return cur

        return closest