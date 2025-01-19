# -*- coding: utf-8 -*-

import logging
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10

        if result > 2 ** 31 - 1:
            return 0

        return result


def run():
    pass


if __name__ == "__main__":
    run()