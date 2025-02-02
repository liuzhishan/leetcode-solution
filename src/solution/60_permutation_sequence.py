# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:
            return ""

        factorial = [1 for _ in range(n + 1)]

        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        res = []
        nums = [i for i in range(1, n + 1)]
        k -= 1

        for i in range(n - 1, -1, -1):
            index = k // factorial[i]
            res.append(nums[index])
            nums.pop(index)
            k %= factorial[i]

        return ''.join([str(x) for x in res])