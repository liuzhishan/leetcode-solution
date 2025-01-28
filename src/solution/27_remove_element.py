# -*- coding: utf-8 -*-

from typing import Optional, List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        pos = 0
        last = n - 1
        cnt = 0

        while pos <= last:
            if nums[pos] == val:
                while last > pos and nums[last] == val:
                    cnt += 1
                    last -= 1

                cnt += 1
                if last > pos:
                    nums[pos], nums[last] = nums[last], nums[pos]
                    pos += 1
                    last -= 1
                else:
                    break
            else:
                pos += 1

        return n - cnt