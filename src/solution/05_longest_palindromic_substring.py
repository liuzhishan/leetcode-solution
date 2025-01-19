# -*- coding: utf-8 -*-

import logging
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format="[%(filename)s:%(lineno)s - %(funcName)s] - %(message)s")


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        odd_center_arr = [[i] for i in range(n)]
        even_center_arr = [[] for _ in range(n)]

        max_length = 1
        max_index = 0

        for i in range(1, n):
            for center in odd_center_arr[i - 1]:
                dist = i - center - 1
                if dist >= 0 and center - dist - 1 >= 0 and s[center - dist - 1] == s[i]:
                    odd_center_arr[i].append(center)

                    if max_length < 2 * dist + 1 + 2:
                        max_length = 2 * dist + 1 + 2
                        max_index = i

            for center in even_center_arr[i - 1]:
                dist = i - center
                if dist >= 0 and center - dist - 1 >= 0 and s[center - dist - 1] == s[i]:
                    even_center_arr[i].append(center)

                    if max_length < 2 * dist + 2:
                        max_length = 2 * dist + 2
                        max_index = i

            if s[i] == s[i - 1]:
                even_center_arr[i].append(i)

                if max_length < 2:
                    max_length = 2
                    max_index = i

        return s[max_index - max_length + 1: max_index + 1]


def run():
    pass


if __name__ == "__main__":
    run()