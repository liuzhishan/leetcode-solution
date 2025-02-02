# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s1 = []
            count = 1
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    s1.append(str(count))
                    s1.append(s[j - 1])
                    count = 1

            s1.append(str(count))
            s1.append(s[-1])
            s = ''.join(s1)
            s1 = []

        return s