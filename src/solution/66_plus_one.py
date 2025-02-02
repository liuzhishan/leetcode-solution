# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return [1]

        res = [x for x in digits]

        carry = 0
        res[n - 1] += 1

        for i in range(n - 1, -1, -1):
            if res[i] >= 10:
                res[i] = 0
                if i == 0:
                    res.insert(0, 1)
                else:
                    res[i - 1] += 1
            else:
                break

        return res