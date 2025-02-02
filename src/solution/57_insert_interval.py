# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)

        if n == 0 or newInterval[0] < intervals[0][0]:
            res.append(newInterval.copy())

        for i in range(n):
            if len(res) > 0:
                if res[-1][0] <= newInterval[0] and newInterval[0] <= intervals[i][0]:
                    if res[-1][1] >= newInterval[0]:
                        res[-1][1] = max(res[-1][1], newInterval[1])
                    else:
                        res.append(newInterval.copy())

                if res[-1][1] >= intervals[i][0]:
                    res[-1][1] = max(res[-1][1], intervals[i][1])
                else:
                    res.append(intervals[i].copy())
            else:
                res.append(intervals[i].copy())

        if res[-1][1] >= newInterval[0]:
            res[-1][1] = max(res[-1][1], newInterval[1])
        else:
            res.append(newInterval.copy())

        return res
