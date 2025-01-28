# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """思考子问题的结构。

        在中间任意位置时，要判断是否包含 words 中的词，假设 words 中的词长度为 m, 则必须往后看 m 个字符。
        前面已经见过的信息可以保存起来。用 dict 报存已经见过的单词与目标的差异。
        """
        if len(words) == 0:
            return []

        res = []
        n = len(words)
        m = len(words[0])
        l = len(s)

        for i in range(m):
            if i + n * m > l:
                break

            d = {}
            for j in range(n):
                word = s[i + j * m: i + (j + 1) * m]
                d[word] = d.get(word, 0) + 1

            for w in words:
                if w not in d:
                    d[w] = 0

                d[w] -= 1
                if d[w] == 0:
                    d.pop(w)

            if len(d) == 0:
                res.append(i)

            for start in range(i + m, l - m * n + 1, m):
                x = s[start + (n - 1) * m: start + n * m]
                d[x] = d.get(x, 0) + 1

                if d[x] == 0:
                    d.pop(x)

                w = s[start - m: start]
                d[w] = d.get(w, 0) - 1

                if d[w] == 0:
                    d.pop(w)
                
                if len(d) == 0:
                    res.append(start)

        return res
