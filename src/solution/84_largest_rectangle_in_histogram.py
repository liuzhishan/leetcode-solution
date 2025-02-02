# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        
        left_arr = [0 for i in range(n)]
        right_arr = [n - 1 for i in range(n)]

        stack = [0]
        for i in range(1, n):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                right_arr[stack[-1]] = i - 1
                stack.pop()

            if len(stack) > 0:
                left_arr[i] = stack[-1] + 1
            else:
                left_arr[i] = 0

            stack.append(i)

        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (right_arr[i] - left_arr[i] + 1))

        return max_area