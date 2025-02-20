题目链接: [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

题目描述: 

```
给定一个字符串 `s`，请你找出其中不含有重复字符的最长子串的长度。
```

## 拆解子问题与循环不变式

我们首先手动尝试几个示例:

`s = "abcabcbb"`, 从头开始最长的无重复子串是 `abc`, 长度为 `3`。再往后到字符 `a` 时，发现 `a` 已经出现过，因此 `abca` 不算。
那么如何找以第四个字符 `a` 结尾的无重复子串呢? 我们可以从这个字符开始往前找，发现 `bca` 无重复字符，长度也是 `3`。后面的字符也可以类似分析。

此时我们对问题有了很清楚的认识，并且很容易想到一个思路，那就是在遍历每个字符时，往前找最长的无重复子串，然后取最大的长度。

如何利用之前的子问题获取的信息呢?

我们从 `0` 到 `len(s) - 1` 遍历每个位置，子问题则为到 `i` 为止的最长无重复子串长度。我们不需要关心 `0~i-1` 的解是如何得出的，
只需要知道这些解已经存在。我们用数组 `arr` 来保存这些解。`....ab` 表示当前的问题，`b` 是当前位置 `i` 的字符，`a` 则是前一个
字符，那么 `arr[i - 1]` 就表示从 `a` 开始往前的无重复子串的长度。我们考虑 `b` 和之前子串的关系:
- 如果 `b` 不在 `arr[i - 1]` 对应的子串中，那么显然 `b` 可以直接加到子串中则是无重复子串， `arr[i] = arr[i - 1] + 1`。
- 如果 `b` 在 `arr[i - 1]` 中，假设其下表为 `pos`, 那么 `pos + ` 到当前的 `b` 则是无重复的子串，可以得出: `arr[i] = i - pos + 1`。

如何得到 `i` 位置之前 `b` 的下标呢? 稍微想一下就发现很简单，我们只需要在遍历的时候每个字符的下标保存起来即可。

经过观察，我们发现还有以下优化点:
- 为了加速下标的查找，我们直接用字符对应的 ASCII 码作为下标，然后用一个长度为 `128` 的数组来保存每个字符的下标。
- 每次我们只用到了 `i - 1` 的解，并不需要保存之前的所有解，因此我们可以直接用一个变量 `last_length` 来保存 `i - 1` 的解。

至此，则得到了完整的解法。

为了实现正确的代码，我们将以上思路转换为如下循环不变式:

`arr[i]` 表示以 `s[i]` 结尾的最长无重复子串的长度, 数组 `d` 表示每个字符 `s[i]` 之前最后一次出现的下标。`-1` 表示未出现过。
- 初始化: 显然 `arr[0] = 1`。
- 保持: 
  - `i - 1` 对应的最长无重复子串的开始位置为: `i - 1 - arr[i - 1] + 1 = i - arr[i - 1]`。
  - 如果 `s[i]` 不在 `arr[i - 1]` 中，即 `d[s[i]] == -1` 或者 `d[s[i]] < i - arr[i - 1]`，那么显然 `arr[i] = arr[i - 1] + 1`。
  - 如果 `s[i]` 在 `arr[i - 1]` 中，即 `d[s[i]] >= i - arr[i - 1]`，则可以得出: `arr[i] = i - d[s[i]] + 1`。
- 终止: 遍历完 `s` 后，`arr` 中保存了以每个字符结尾的最长无重复子串的长度。

**注意**: 在后续的讲解中，不会明显区分拆解子问题和循环不变式，而是将两者结合起来讲解。

## 代码实现

基于以上思路和分析，我们可以实现如下代码:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """用 ord 加速下标的索引。

        循环不变式: `arr[i]` 表示以 `s[i]` 结尾的最长无重复子串的长度, 数组 `d` 表示每个字符 `s[i]` 之前最后一次出现的下标。`-1` 表示未出现过。
        - 初始化: 显然 `arr[0] = 1`。
        - 保持: 
          - `i - 1` 对应的最长无重复子串的开始位置为: `i - 1 - arr[i - 1] + 1 = i - arr[i - 1]`。
          - 如果 `s[i]` 不在 `arr[i - 1]` 中，即 `d[s[i]] == -1` 或者 `d[s[i]] < i - arr[i - 1]`，那么显然 `arr[i] = arr[i - 1] + 1`。
          - 如果 `s[i]` 在 `arr[i - 1]` 中，即 `d[s[i]] >= i - arr[i - 1]`，则可以得出: `arr[i] = i - d[s[i]] + 1`。
        - 终止: 遍历完 `s` 后，`arr` 中保存了以每个字符结尾的最长无重复子串的长度。
        """
        max_length = 0
        last_length = 0
        d = [-1 for _ in range(128)]

        for i in range(len(s)):
            cur = ord(s[i])
            if d[cur] == -1:
                last_length += 1
            else:
                pos = d[cur]
                if pos >= i - last_length:
                    last_length = i - pos
                else:
                    last_length += 1

            d[cur] = i

            max_length = max(last_length, max_length)

        return max_length
```