# -*- coding: utf-8 -*-

from typing import Optional, List


class Solution:
    """线根据 needle 建立索引，对于位置 pos, 记录 [start, x] == [y, pos] 的最大长度, 即从开头的子串与
    以当前字符结尾的子串相等时候的最大的长度，且不能包含当前字符。
    """
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return -1

        table = [0 for _ in range(n)]

        for i in range(1, n):
            if needle[i] == needle[table[i - 1]]:
                table[i] = table[i - 1] + 1
            else:
                j = table[i - 1]
                while j > 0 and j != table[j - 1] and needle[i] != needle[j]:
                    j = table[j - 1]

                if needle[i] == needle[j]:
                    table[i] = j + 1

        arr = [0 for _ in range(len(haystack))]

        for i in range(len(haystack)):
            if i == 0:
                if haystack[i] == needle[i]:
                    arr[i] = 1
            else:
                if haystack[i] == needle[arr[i - 1]]:
                    arr[i] = arr[i - 1] + 1
                else:
                    j = arr[i - 1]
                    while j > 0 and j != table[j - 1] and haystack[i] != needle[j]:
                        j = table[j - 1]

                    if haystack[i] == needle[j]:
                        arr[i] = j + 1

            if arr[i] == n:
                return i - n + 1

        return -1