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

        循环不变式: `arr[i]` 表示以 `s[i]` 结尾的最长无重复子串的长度, 数组 `d` 表示每个字符 `s[i]` 之前最后一次出现的下标。`-1` 表示未出现过。
        - 初始化: 显然 `arr[0] = 1`。
        - 保持: 
          - `i - 1` 对应的最长无重复子串的开始位置为: `i - 1 - arr[i - 1] + 1 = i - arr[i - 1]`。
          - 如果 `s[i]` 不在 `arr[i - 1]` 中，即 `d[s[i]] == -1` 或者 `d[s[i]] < i - arr[i - 1]`，那么显然 `arr[i] = arr[i - 1] + 1`。
          - 如果 `s[i]` 在 `arr[i - 1]` 中，即 `d[s[i]] >= i - arr[i - 1]`，则可以得出: `arr[i] = i - d[s[i]] + 1`。
        - 终止: 遍历完 `s` 后，`arr` 中保存了以每个字符结尾的最长无重复子串的长度。
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