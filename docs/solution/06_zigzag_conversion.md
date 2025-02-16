题目链接: [6. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/)

题目描述

```
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
```

## 拆解子问题与循环不变式

这道题目根据提议模拟规则即可。输出位一个二维 `table` 数组。我们可以将从头开始的字符串作为子问题，`table` 则表示当前字符串
对应的结果，因此只需考虑当前字符如何处理即可。并且我们观察到 `table` 行数是固定的，每一行里的字符都是逐个往里添加，因此只需要
遍历行即可。

以题目中的字符串为例, 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

```
P   A   H   N
A P L S I I G
Y   I   R
```

循环不变式: `table` 是最终结果对应的二维数组, `y` 是当前字符在 `table` 中的行, `direction` 表示方向, `1` 向下, `-1` 向上。
当遇到字符 `s[i]` 时, 将其 `append` 到 `table[y]` 中，然后更新 `y` 和 `direction` 即可。
- 如果 `direction` 为 `1`，则 `y` 向下移动，如果 `y < numRows - 1`，则 `y` 继续向下一步, `y = (y + 1) % numRows`, 否则
`direction` 变为 `-1`, `y = max(y - 1, 0)`。
- 如果 `direction` 为 `-1`，则 `y` 向上移动，如果 `y > 0`，则 `y` 继续向上一步, `y = max(y - 1, 0)`, 否则 `direction`
变为 `1`, `y = min(y + 1, numRows - 1)`。


## 代码实现

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        table = [[] for _ in range(numRows)]

        y = 0

        # 1: down, -1: up
        direction = 1

        for i in range(len(s)):
            table[y].append(s[i])

            if direction == 1:
                if y < numRows - 1:
                    y = (y + 1) % numRows
                else:
                    direction = -1
                    y = max(y - 1, 0)
            else:
                if y > 0:
                    y = max(y - 1, 0)
                else:
                    direction = 1
                    y = (y + 1) % numRows

        return ''.join([''.join(row) for row in table])
```