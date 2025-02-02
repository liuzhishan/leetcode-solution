# -*- coding: utf-8 -*-

from typing import List, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]

        res = []
        col_visited = [False for _ in range(n)]

        self.dfs(board, col_visited, 0, res)

        return res

    def dfs(self, board: List[List[str]], col_visited: List[bool], row: int, res: List[List[str]]):
        if row == len(board):
            res.append([''.join(row) for row in board])
            return

        for col in range(len(board)):
            if col_visited[col]:
                continue

            is_valid = True

            x, y = row, col
            dir_x, dir_y = -1, -1
            for i in range(len(board)):
                x, y = x + dir_x, y + dir_y
                if x < 0 or x >= len(board) or y < 0 or y >= len(board):
                    break

                if board[x][y] == 'Q':
                    is_valid = False
                    break

            if is_valid:
                x, y = row, col
                dir_x, dir_y = -1, 1
                for i in range(len(board)):
                    x, y = x + dir_x, y + dir_y
                    if x < 0 or x >= len(board) or y < 0 or y >= len(board):
                        break

                    if board[x][y] == 'Q':
                        is_valid = False
                        break

            if not is_valid:
                continue

            board[row][col] = 'Q'
            col_visited[col] = True

            self.dfs(board, col_visited, row + 1, res)

            board[row][col] = '.'
            col_visited[col] = False