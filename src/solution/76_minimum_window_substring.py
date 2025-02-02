# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        d = {}
        for c in t:
            d[c] = d.get(c, 0) - 1

        count_char = len(d)

        start = -1
        end = -1
        total = 0

        for i in range(n):
            if s[i] in d:
                d[s[i]] += 1
                if start == -1:
                    start = i

                if d[s[i]] == 0:
                    total += 1

                if total == count_char:
                    end = i
                    break

        if start == -1 or end == -1:
            return ""

        for k in d:
            if d[k] < 0:
                return ""

        for i in range(start, end + 1):
            if s[i] not in d:
                continue
            if d[s[i]] > 0:
                d[s[i]] -= 1
            else:
                start = i
                break

        min_start = start
        min_end = end
        min_length = end - start + 1

        for i in range(end + 1, n):
            if s[i] in d:
                d[s[i]] += 1

                while start < i and (s[start] not in d or d[s[start]] > 0):
                    if s[start] in d:
                        d[s[start]] -= 1
                    start += 1

                if i - start + 1 < min_length:
                    min_start = start
                    min_end = i
                    min_length = i - start + 1

        return s[min_start:min_end + 1]
