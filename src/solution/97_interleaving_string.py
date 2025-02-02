# -*- coding: utf-8 -*-

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        n1 = len(s1)
        n2 = len(s2)

        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = True

        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])

        return dp[n1][n2]
        