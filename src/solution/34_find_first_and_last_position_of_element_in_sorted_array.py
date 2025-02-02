# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        lower_bound = -1
        upper_bound = -1

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if left < n and nums[left] == target:
            lower_bound = left
        else:
            return [-1, -1]

        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if right >= 0 and nums[right] == target:
            upper_bound = right
        else:
            return [-1, -1]
        
        return [lower_bound, upper_bound]