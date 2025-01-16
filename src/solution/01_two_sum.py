# -*- coding: utf-8 -*-

import logging
from typing import List

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, x in enumerate(nums):
            if target - x in d:
                return [d[target - x], i]
            d[x] = i

        return []


def run():
    solution = Solution()
    logging.info(solution.twoSum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    run()