# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)

        a1 = [int(x) for x in a][::-1]
        b1 = [int(x) for x in b][::-1]

        res = [0 for x in range(max(n, m) + 1)]

        carry = 0
        for i in range(max(n, m)):
            res[i] = carry
            if i < n:
                res[i] += a1[i]
            if i < m:
                res[i] += b1[i]

            if res[i] >= 2:
                res[i] = res[i] % 2
                carry = 1
            else:
                carry = 0

        if carry == 1:
            res[max(n, m)] = 1

        if res[max(n, m)] == 0:
            res = res[:-1]

        return ''.join([str(x) for x in res[::-1]])