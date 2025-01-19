# -*- coding: utf-8 -*-

import logging
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        二分查找。
        """
        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)

        # 假如找到中位数，那么应该分别在 nums1 和 nums2 中有左半边。nums1 的右端点小于 nums2 的右半边的第一个数，
        # 且 nums2 的右端点小于 nums1 的右半边的第一个数。否则，继续在 nums1 中二分。
        i_min, i_max = 0, n
        mid = (i_min + i_max) // 2

        half_len = (n + m + 1) // 2
        j = half_len - mid

        # i_min, i_max 是 nums1 的二分查找范围。
        # half_len 是 nums1 和 nums2 的左半边的总长度。
        # mid 是 nums1 左半边的长度，j 是 nums2 左半边的长度。
        while i_min <= i_max:
            mid = (i_min + i_max) // 2
            # j 是 nums2 的二分查找范围。
            j = half_len - mid

            # 比较 nums1 和 nums2 的左半边右端点和右半边的左端点。
            # 如果右端点都大于左端点，则说明找到了。否则，继续二分。
            if mid > 0 and nums2[j] < nums1[mid - 1]:
                i_max = mid - 1
            elif mid < n and j - 1 >= 0 and j - 1 < m and nums1[mid] < nums2[j - 1]:
                i_min = mid + 1
            else:
                break

        if (n + m) % 2 == 1:
            if mid - 1 >= 0 and j - 1 >= 0:
                return max(nums1[mid - 1], nums2[j - 1])
            elif mid - 1 >= 0:
                return nums1[mid - 1]
            else:
                return nums2[j - 1]
        else:
            x = 0
            y = 0

            if mid - 1 >= 0 and j - 1 >= 0:
                x = max(nums1[mid - 1], nums2[j - 1])
            elif mid - 1 >= 0:
                x = nums1[mid - 1]
            else:
                x = nums2[j - 1]

            if mid < n and j < m:
                y = min(nums1[mid], nums2[j])
            elif mid < n:
                y = nums1[mid]
            else:
                y = nums2[j]

            return (x + y) / 2


def run():
    solution = Solution()

    nums1 = [1, 3]
    nums2 = [2]
    logging.info(solution.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
    run()