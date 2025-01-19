# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }

        powers = []
        digits = []

        x = num
        p = 1

        while x > 0:
            powers.append(p)
            digits.append(x % 10)

            x //= 10
            p *= 10

        powers = powers[::-1]
        digits = digits[::-1]

        res = ['' for _ in range(len(powers))]
        
        for i, x in enumerate(powers):
            if digits[i] == 0:
                continue

            if digits[i] < 4:
                res[i] = d[powers[i]] * digits[i]
            elif digits[i] == 4 or digits[i] == 9:
                res[i] = d[powers[i]] + d[powers[i] * (digits[i] + 1)]
            else:
                res[i] = d[powers[i] * 5] + d[powers[i]] * (digits[i] - 5)

        return ''.join(res)