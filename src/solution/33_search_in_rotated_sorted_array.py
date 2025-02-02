# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[mid] < target:
                    left = mid + 1
                elif target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] > target:
                    right = mid - 1
                elif target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
