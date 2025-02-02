# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False

        if len(word) == 0:
            return True

        n = len(board)
        m = len(board[0])

        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.search(board, word, n, m, i, j, 0, visited):
                        return True

        return False

    def search(
        self,
        board: List[List[str]],
        word: str,
        n: int,
        m: int,
        x: int,
        y: int,
        index: int,
        visited: List[List[bool]],
    ) -> bool:
        if index == len(word):
            return True

        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        if visited[x][y]:
            return False

        if board[x][y] != word[index]:
            return False

        visited[x][y] = True

        if self.search(board, word, n, m, x + 1, y, index + 1, visited):
            return True

        if self.search(board, word, n, m, x - 1, y, index + 1, visited):
            return True

        if self.search(board, word, n, m, x, y + 1, index + 1, visited):
            return True

        if self.search(board, word, n, m, x, y - 1, index + 1, visited):
            return True

        visited[x][y] = False

        return False
