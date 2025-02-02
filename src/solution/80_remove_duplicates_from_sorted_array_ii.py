# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        n = len(nums)

        i = 0
        
        for j in range(n):
            if i < 2 or nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i