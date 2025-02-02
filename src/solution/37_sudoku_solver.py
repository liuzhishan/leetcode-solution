# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        candidates = [[[True for _ in range(9)] for _ in range(9)] for _ in range(9)]

        x_candidates = [[True for _ in range(9)] for _ in range(9)]
        y_candidates = [[True for _ in range(9)] for _ in range(9)]
        z_candidates = [[[True for _ in range(9)] for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x_candidates[i][ord(board[i][j]) - ord('1')] = False
                    y_candidates[j][ord(board[i][j]) - ord('1')] = False
                    z_candidates[i // 3][j // 3][ord(board[i][j]) - ord('1')] = False

        total = sum([1 if board[i][j] == '.' else 0 for i in range(9) for j in range(9)])
        cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']

        self.dfs(board, x_candidates, y_candidates, z_candidates, cells, 0)

    def dfs(
            self,
            board: List[List[str]],
            x_candidates: List[List[bool]],
            y_candidates: List[List[bool]],
            z_candidates: List[List[List[bool]]],
            cells: List[Tuple[int, int]],
            index: int
    ) -> bool:
        if index == len(cells):
            return True

        x, y = cells[index]

        nums = []
        for num in range(9):
            if x_candidates[x][num] and y_candidates[y][num] and z_candidates[x // 3][y // 3][num]:
                nums.append(num)

        if len(nums) == 0:
            return False

        for num in nums:
            board[x][y] = str(num + 1)
            x_candidates[x][num] = False
            y_candidates[y][num] = False
            z_candidates[x // 3][y // 3][num] = False

            if self.dfs(board, x_candidates, y_candidates, z_candidates, cells, index + 1):
                return True

            board[x][y] = '.'
            x_candidates[x][num] = True
            y_candidates[y][num] = True
            z_candidates[x // 3][y // 3][num] = True

        return False