# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        if len(s) == 0:
            return False

        n = len(s)

        # +
        count_pos = 0
        # -
        count_neg = 0
        # .
        count_dot = 0
        # e
        count_e = 0
        # digit
        count_digit = 0

        for i in range(n):
            if s[i] == '+':
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if i == n - 1:
                    return False
                count_pos += 1
            elif s[i] == '-':
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if i == n - 1:
                    return False
                count_neg += 1
            elif s[i] == '.':
                if count_dot > 0 or count_e > 0:
                    return False
                if i > 0 and (s[i - 1].isdigit() or s[i - 1] == '+' or s[i - 1] == '-'):
                    count_dot += 1
                    continue
                elif i == 0:
                    count_dot += 1
                    continue
                else:
                    return False
            elif s[i] == 'e' or s[i] == 'E':
                if count_e > 0 or i == 0 or i == n - 1 or (i - 1 >= 0 and not s[i - 1].isdigit() and s[i - 1] != '.'):
                    return False
                if count_digit == 0:
                    return False
                count_e += 1
            elif s[i] == ' ':
                return False
            elif s[i].isdigit():
                count_digit += 1
                continue
            elif s[i].isalpha():
                return False

        if count_digit == 0:
            return False
        
        return True
