# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 注意从后面开始，否则会覆盖。
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]

        pos = 0
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i + n] < nums2[j]:
                nums1[pos] = nums1[i + n]
                i += 1
            else:
                nums1[pos] = nums2[j]
                j += 1

            pos += 1

        if i < m:
            for k in range(i, m):
                nums1[pos] = nums1[k + n]
                pos += 1
        else:
            for k in range(j, n):
                nums1[pos] = nums2[k]
                pos += 1