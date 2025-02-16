题目链接: [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)

题目描述

```
给你一个字符串 s，找到 s 中最长的回文子串。
```

## 拆解子问题与循环不变式

最容易想到的思路就是在每个位置同时向两边扩展来判断是否是回文子串，然后取最长的即可。

我们思考下有没有更快的解法。

还是先手动尝试几个示例:
- `s` 长度为 `1`, `s = a`, 显然最长回文子串就是 `a`。
- `s` 长度为 `2`, `s = ab`, 显然最长回文子串就是 `a` 或 `b`, 如果字符相等，如 `s = aa`, 则结果为 `aa`。
- `s` 长度为 `3`, `s = abc`, 显然最长回文子串就是 `a` 或 `b` 或 `c`, 如果是对称的字符串, 如 `s = aba`, 则结果为 `aba`。
- `s` 长度为 `4`, `s = abba`, 显然最长回文子串就是 `abba`, 这刚好是对称的结果，回文子串长度为偶数。

通过这些示例，我们发现回文的长度可以是偶数，也可以是奇数。

我们将题目换种说法，求以每个字符结尾的回文串，然后取最大值。

现在考虑如何拆解子问题。`s` 的长度为 `n`, 我们在长度维度上来减小问题, 采用线性遍历的方式。

循环不变式: `s[..i]` 表示子问题, `arr[i]` 表示以 `s[i]` 结尾的回文子串的长度。这里又需要思考一下，以 `s[i]` 字符结尾可能有多个回文串,
是保留最长的一个还是都保留? 当前不是最长的后面有可能发展为最长的，所以应该是都保留。而回文串长度可能是奇数，也可能是偶数，我们需要两个数组来
保存, 同时考虑到中心位置方便计算下标，也能提供长度, 因此用 `odd_center_arr[i]` 保存奇数长度的回文串中心位置，用 `even_center_arr[i]`
保存偶数长度的回文串中心位置。

如下所示, 当前字符为 `b`, `axxxa` 表示以 `a` 结尾的奇数回文串, `baxxxab` 则是以当前字符结尾的更长的回文串。

```
....baxxxab
```

当在位置 `i` 时, 以奇数回文串为例，我们知道 `s[i - 1]` 存在一些回文串, 如果 `s[i]` 是某个回文串的结尾，则必定与 `s[i - 1]` 的回文串
开头再往前的一个字符相等。因此我们判断 `s[i]` 是否与这一字符相等即可知道 `s[i]` 是否是奇数回文串的结尾, 更新 `odd_center_arr[i]` 即可。

偶数回文串同理。

这样我们就求得了以每个 `s[i]` 结尾的奇数回文串和偶数回文串, 再取其中的最大值即可。

## 代码实现

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        odd_center_arr = [[i] for i in range(n)]
        even_center_arr = [[] for _ in range(n)]

        max_length = 1
        max_index = 0

        for i in range(1, n):
            for center in odd_center_arr[i - 1]:
                dist = i - center - 1
                if dist >= 0 and center - dist - 1 >= 0 and s[center - dist - 1] == s[i]:
                    odd_center_arr[i].append(center)

                    if max_length < 2 * dist + 1 + 2:
                        max_length = 2 * dist + 1 + 2
                        max_index = i

            for center in even_center_arr[i - 1]:
                dist = i - center
                if dist >= 0 and center - dist - 1 >= 0 and s[center - dist - 1] == s[i]:
                    even_center_arr[i].append(center)

                    if max_length < 2 * dist + 2:
                        max_length = 2 * dist + 2
                        max_index = i

            if s[i] == s[i - 1]:
                even_center_arr[i].append(i)

                if max_length < 2:
                    max_length = 2
                    max_index = i

        return s[max_index - max_length + 1: max_index + 1]
```