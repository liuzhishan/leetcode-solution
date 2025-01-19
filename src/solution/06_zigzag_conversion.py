# -*- coding: utf-8 -*-

import logging
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        table = [[] for _ in range(numRows)]

        # 循环不变式: 
        # 1. direction 表示方向，1 表示向下，-1 表示向上。
        # 2. x, y 分别表示当前字符在 table 中的位置, y 表示行，x 表示列。
        #
        # 初始化:
        # 保持:
        # 终止:
        x = 0
        y = 0

        # 1: down, -1: up
        direction = 1

        for i in range(len(s)):
            table[y].append(s[i])

            if direction == 1:
                if y < numRows - 1:
                    if (y + 1) % numRows == y:
                        x += 1
                    y = (y + 1) % numRows
                else:
                    direction = -1
                    y = max(y - 1, 0)
                    x = x + 1
            else:
                if y > 0:
                    y = max(y - 1, 0)
                    x = x + 1
                else:
                    direction = 1
                    if (y + 1) % numRows == y:
                        x += 1
                    y = (y + 1) % numRows

        return ''.join([''.join(row) for row in table])


def run():
    pass


if __name__ == "__main__":
    run()