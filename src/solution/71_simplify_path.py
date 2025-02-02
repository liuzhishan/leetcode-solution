# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split('/'):
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            elif p == '.' or p == '':
                continue
            else:
                stack.append(p)

        return '/' + '/'.join(stack)