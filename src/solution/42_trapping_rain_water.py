# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        water = 0

        for i in range(n):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                left = stack.pop()
                if len(stack) == 0:
                    break
                water += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[left])

            stack.append(i)

        return water

            