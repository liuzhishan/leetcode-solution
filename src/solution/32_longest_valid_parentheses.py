# -*- coding: utf-8 -*-


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        # 记录以 i 结尾的最长有效子串的长度
        arr = [0 for _ in range(n)]

        for i in range(1, n):
            if s[i] == '(':
                continue
            else:
                if s[i - 1] == '(':
                    arr[i] = arr[i - 2] + 2
                else:
                    if i - arr[i - 1] - 1 >= 0 and s[i - arr[i - 1] - 1] == '(':
                        arr[i] = arr[i - 1] + 2
                        if i - arr[i - 1] - 2 >= 0:
                            arr[i] += arr[i - arr[i - 1] - 2]

        return max(arr)