class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1

        sign = 1

        if x < 0:
            if n % 2 == 0:
                x = -x
            else:
                x = -x
                sign = -1

        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        if n % 2 == 0:
            return self.myPow(x * x, n // 2) * sign
        else:
            return self.myPow(x * x, n // 2) * x * sign