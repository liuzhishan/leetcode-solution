题目链接: [28. 找出字符串中第一个匹配项的下标](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)

题目描述:

```
给定一个字符串 `haystack` 和一个字符串 `needle`，在 `haystack` 中找出 `needle` 的第一个匹配项的下标（从 0 开始）。
如果不存在，则返回 `-1`。
```

## 拆解子问题与循环不变式

我们首先手动尝试几个示例:

`haystack = "hello", needle = "ll"`，显然 `ll` 在 `hello` 中第一次出现的位置是 `2`。

最容易想到的方法是遍历每个 `haystack` 的字符，然后从当前字符开始往前进行匹配，如果匹配到了 `needle` 则返回当前位置。但是这一思路
有很多重复计算，很多字符会被比较多次，有没有办法减少重复计算呢？

我们直接进入到分析位置 `i` 的环节。注意，子问题不一定是题目所要的解，我们也可能需要提出其他中间问题。假如 `i - 1` 已经匹配上了 `needle`
中的一部分子串，即前缀子串，那么分析 `i` 位置的匹配情况，思考 `i - 1` 位置有哪些信息可以利用。

循环不变式为: `arr[i]` 表示以 `haystack` 位置 `i` 结尾的子串匹配 `needle` 前缀的最大长度。
- 如果位置 `i` 也匹配，那么皆大欢喜，继续往后匹配即可。如果长度已经等于 `len(needle)`, 则说明已经找到匹配。
- 如果位置 `i` 不匹配，其可能会匹配到前面的某个位置，那么需要从 `i - len(needle) + 1` 位置重新开始和 `needle` 进行比较。从头
开始比较太浪费了。假如 `i - 1` 位置可以告诉我们其最大可以匹配的前缀位置, 就能节省很多比较次数。我们还是按之前的思路，假设已经知道
这一答案。


## 代码实现

```python
class Solution:
    """根据 needle 建立索引，对于位置 pos, 记录 [start, x] == [y, pos] 的最大长度, 即从开头的子串与
    以当前字符结尾的子串相等时候的最大的长度，且不能包含当前字符。
    """
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return -1

        table = [0 for _ in range(n)]

        for i in range(1, n):
            if needle[i] == needle[table[i - 1]]:
                table[i] = table[i - 1] + 1
            else:
                j = table[i - 1]
                while j > 0 and j != table[j - 1] and needle[i] != needle[j]:
                    j = table[j - 1]

                if needle[i] == needle[j]:
                    table[i] = j + 1

        arr = [0 for _ in range(len(haystack))]

        for i in range(len(haystack)):
            if i == 0:
                if haystack[i] == needle[i]:
                    arr[i] = 1
            else:
                if haystack[i] == needle[arr[i - 1]]:
                    arr[i] = arr[i - 1] + 1
                else:
                    j = arr[i - 1]
                    while j > 0 and j != table[j - 1] and haystack[i] != needle[j]:
                        j = table[j - 1]

                    if haystack[i] == needle[j]:
                        arr[i] = j + 1

            if arr[i] == n:
                return i - n + 1

        return -1
```