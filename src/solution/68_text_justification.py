# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        n = len(words)
        i = 0

        while i < n:
            j = i
            cur_len = 0
            while j < n:
                if cur_len + len(words[j]) + j - i > maxWidth:
                    break
                cur_len += len(words[j])
                j += 1

            if j == n:
                s1 = ' '.join(words[i:j])
                res.append(s1 + ' ' * (maxWidth - len(s1)))
                break

            a = maxWidth - cur_len
            remain = 0
            if j - i > 1:
                a = (maxWidth - cur_len) // (j - i - 1)
                remain = (maxWidth - cur_len) % (j - i - 1)

            arr = []
            for k in range(i, j):
                arr.append(words[k])
                if k < j - 1:
                    arr.append(' ' * a)
                    if remain > 0:
                        arr.append(' ')
                        remain -= 1

            s2 = ''.join(arr)
            res.append(s2 + ' ' * (maxWidth - len(s2)))

            if i == j:
                i += 1
            else:
                i = j

        return res
