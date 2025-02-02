# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        pos = n - 1
        while pos > 0:
            if nums[pos] > nums[pos - 1]:
                break
            pos -= 1

        if pos == 0:
            nums.sort()
            return

        # 寻找比 nums[pos - 1] 大的最小值
        min_val = nums[pos]
        min_pos = pos
        for i in range(pos, n):
            if nums[i] > nums[pos - 1] and nums[i] < min_val:
                min_val = nums[i]
                min_pos = i

        nums[pos - 1], nums[min_pos] = nums[min_pos], nums[pos - 1]
        nums[pos:] = sorted(nums[pos:])
