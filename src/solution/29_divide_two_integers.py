# -*- coding: utf-8 -*-


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        sign = 1
        if dividend < 0 and divisor > 0:
            sign = -1
        if dividend > 0 and divisor < 0:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        x = divisor
        cnt = 1
        while x < dividend:
            if x + x < dividend:
                x += x
                cnt += cnt
            elif x + x == dividend:
                x += x
                cnt += cnt
                break
            else:
                cnt += self.divide(dividend - x, divisor)
                break

        res = cnt * sign

        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31
        else:
            return res
