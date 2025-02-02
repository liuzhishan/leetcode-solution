# -*- coding: utf-8 -*-

from typing import List, Optional


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        n = len(s)
        arr = [0 for _ in range(n + 1)]

        if s[0] == '0':
            return 0

        arr[0] = 1

        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    if i >= 2:
                        arr[i] = arr[i - 2]
                    else:
                        arr[i] = 1
                else:
                    return 0
            else:
                if (s[i - 1] == '1' or s[i - 1] == '2') and int(s[i - 1:i + 1]) <= 26:
                    if i >= 2:
                        arr[i] = arr[i - 1] + arr[i - 2]
                    else:
                        arr[i] = 2
                else:
                    arr[i] = arr[i - 1]

        return arr[n - 1]
