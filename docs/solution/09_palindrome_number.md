题目链接: [9. 回文数](https://leetcode.cn/problems/palindrome-number/)

题目描述

```
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
```

## 拆解子问题与循环不变式

根据题意，先求出 `x` 反转后的数，再判断是否相等即可。反转的逻辑可以参考之前的题目 [07_reverse_integer.md](solution/07_reverse_integer.md)。


## 代码实现

```python
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
```
