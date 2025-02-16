题目链接: [8. 字符串转换整数 (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/)

题目描述

```
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。
```

## 拆解子问题与循环不变式

字符串 `s` 可以看做是字符数组，按为遍历即可, 即子问题为从头开始到 `s[i]` 的子字符串。`res` 为结果, `res` 只依赖于当前字符以及 `res[i - 1]`, 因此
可以省略 `res` 数组, 用一个变量来保存结果。

循环不变式: 假设循环开始前 `res` 为从头开始到 `s[i - 1]` 对应的结果，则 `res = res * 10 + s[i]`。

再考虑各种规则即可, 比如正负号、空格、非数字、溢出等等，有点繁琐，不再展开。


## 代码实现

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0

        # 1: positive, -1: negative
        sign = 1
        after_sign = False

        for (i, c) in enumerate(s):
            if c == ' ':
                if after_sign:
                    break
                continue
            elif c == '+':
                if after_sign:
                    break
                sign = 1
                after_sign = True
            elif c == '-':
                if after_sign:
                    break
                sign = -1
                after_sign = True
            elif c.isdigit():
                res = res * 10 + int(c)
                after_sign = True
            else:
                break

        res = res * sign

        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31

        return res
```

