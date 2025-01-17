# -*- coding: utf-8 -*-

import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        last_length = 0
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                last_length += 1
            else:
                pos = d[s[i]]
                if pos >= i - last_length:
                    last_length = i - pos
                else:
                    last_length += 1

            d[s[i]] = i

            max_length = max(last_length, max_length)

        return max_length


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """用 ord 加速下标的索引。
        """
        max_length = 0
        last_length = 0
        d = [-1 for _ in range(128)]

        for i in range(len(s)):
            cur = ord(s[i])
            if d[cur] == -1:
                last_length += 1
            else:
                pos = d[cur]
                if pos >= i - last_length:
                    last_length = i - pos
                else:
                    last_length += 1

            d[cur] = i

            max_length = max(last_length, max_length)

        return max_length


def run():
    pass


if __name__ == "__main__":
    run()