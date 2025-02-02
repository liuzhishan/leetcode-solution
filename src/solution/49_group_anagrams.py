# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            s1 = ''.join(sorted(s))
            if s1 not in d:
                d[s1] = []

            d[s1].append(s)

        res = [v for (k, v) in d.items()]
        return res