题目链接: [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/)

题目描述
```
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。
```


## 拆解子问题与循环不变式

这道题逻辑比较简单，我们重点关注下如何用循环不变式来保证代码的正确性。

我们还是先手动尝试几个示例，从简单开始, 分析下题目:
- 题目说了非空，假设两个链表长度都为 `1`，则 `l1 = [1]`, `l2 = [2]`，则 `1 + 2 = 3`，则返回 `[3]`。再复杂点,
`l1 = [9]`, 则结果为 `l1 + l2 = 9 + 2 = 11`，则返回 `[1, 1]`, 我们发现需要考虑进位。
- 假如长度不一样，如 `l1 = [1, 2]`, `l2 = [3, 4, 5]`，则结果为 `l1 + l2 = 21 + 543 = 564`，则返回 `[5, 6, 4]`。

从这些示例我们可以发现，解法基本就是模拟加法运算即可。刚好从 `0` 开始遍历，就是对应加法运算的从最低位计算，同时保留一个进位。

结果需要返回一个链表，我们可以先创建一个 `root` 节点，作为结果链表挂载的结果，最终结果返回 `root.next` 即可。

我们考虑下如何用循环不变式来保证代码的正确性。
循环不变式: `p1`, `p2` 分别表示 `l1` 和 `l2` 的当前节点，`flag` 表示进位, `root` 表示结果链表的头节点, `node` 表示前一次计算后
的结果对应的节点。显然, 初始化 `p1 = l1`, `p2 = l2`, `flag = 0`。
保持阶段，我们可以发现两个数的长度可能会不一样，相加时候以小的那个数为准先计算，再将进位加个大的那个数剩余的部分。所以这部分逻辑整体
框架如下:

```python
while p1 and p2:
    ...
    p1 = p1.next
    p2 = p2.next

while p1 != None:
    ...
    p1 = p1.next

while p2 != None:
    ...
    p2 = p2.next
```

我们再来看下 `...` 对应的计算逻辑，我们的循环不变式涉及 `p1`, `p2`, `flag`, `node` 这 `4` 个变量，只要把这个 `4` 个变量的值都
更新了, 使其满足循环不变式即可。按照加法定义，如下实现:

```python
node.next = ListNode((p1.val + p2.val + flag) % 10)
node = node.next

flag = (p1.val + p2.val + flag) // 10
p1 = p1.next
p2 = p2.next
```

当其中一个数遍历完后，我们只需将进位 `flag` 加给另一个数即可，如下所示:

```python
while p1 != None:
    node.next = ListNode((p1.val + flag) % 10)
    node = node.next
    flag = (p1.val + flag) // 10
    p1 = p1.next
```

`p2` 类似。

最后, 当两个数都遍历完后，还需要考虑 `flag` 不为 `0` 的情况，再加一个位数。

至此，循环不变式的四个变量都满足假设的情况, 则我们就可以理论上保证代码的正确性。

## 代码实现

```python

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        root = ListNode(0)
        flag = 0

        node = root
        while p1 and p2:
            node.next = ListNode((p1.val + p2.val + flag) % 10)
            node = node.next

            flag = (p1.val + p2.val + flag) // 10
            p1 = p1.next
            p2 = p2.next

        while p1 != None:
            node.next = ListNode((p1.val + flag) % 10)
            node = node.next
            flag = (p1.val + flag) // 10
            p1 = p1.next

        while p2 != None:
            node.next = ListNode((p2.val + flag) % 10)
            node = node.next
            flag = (p2.val + flag) // 10
            p2 = p2.next

        if flag != 0:
            node.next = ListNode(flag)
            node = node.next

        return root.next
```