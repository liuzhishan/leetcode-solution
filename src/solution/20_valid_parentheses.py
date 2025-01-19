# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if c == ')' and top != '(':
                    return False
                elif c == ']' and top != '[':
                    return False
                elif c == '}' and top != '{':
                    return False
                else:
                    pass

        return len(stack) == 0