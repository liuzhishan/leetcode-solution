# -*- coding: utf-8 -*-

import logging
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0

        # 1: positive, -1: negative
        sign = 1
        after_sign = False

        for (i, c) in enumerate(s):
            if c == ' ':
                if after_sign:
                    break
                continue
            elif c == '+':
                if after_sign:
                    break
                sign = 1
                after_sign = True
            elif c == '-':
                if after_sign:
                    break
                sign = -1
                after_sign = True
            elif c.isdigit():
                res = res * 10 + int(c)
                after_sign = True
            else:
                break

        res = res * sign

        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31

        return res


def run():
    pass


if __name__ == "__main__":
    run()