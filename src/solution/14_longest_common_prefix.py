# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        pos = 0
        for i in range(len(strs[0])):
            is_same = True

            for j in range(len(strs)):
                if pos >= len(strs[j]):
                    is_same = False
                    break

                if strs[j][pos] != strs[0][pos]:
                    is_same = False
                    break

            if is_same:
                pos += 1
            else:
                break

        return strs[0][:pos]

