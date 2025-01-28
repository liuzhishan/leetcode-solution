# -*- coding: utf-8 -*-

from typing import Optional, List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        pos = 0
        for i in range(1, n):
            if nums[i] != nums[pos]:
                pos += 1
                nums[pos] = nums[i]

        return pos + 1
        

