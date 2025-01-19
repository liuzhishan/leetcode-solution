# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """从左往右构造子问题发现比较麻烦。考虑从两边构造。
        """
        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
