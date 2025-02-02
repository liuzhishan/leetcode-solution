# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """cur_sum 表示以 i - 1 结尾的最大 sum。如果 cur_sum <= 0, 则以当前位置 i 重新开始计数。
        """
        if len(nums) == 0:
            return 0

        res = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            if cur_sum <= 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            res = max(res, cur_sum)

        return res