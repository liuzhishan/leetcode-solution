# -*- coding: utf-8 -*-

import logging
from typing import Optional, List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        a = x
        b = 0

        while a > 0:
            b = b * 10 + a % 10
            a = a // 10

        return b == x