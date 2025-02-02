class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        if n == 0 or m == 0:
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0 for _ in range(n + m)]
        for i in range(n):
            for j in range(m):
                res[i + j] += int(num1[i]) * int(num2[j])

        for i in range(n + m - 1):
            res[i + 1] += res[i] // 10
            res[i] = res[i] % 10

        return ''.join(str(x) for x in res[::-1]).lstrip('0') or "0"