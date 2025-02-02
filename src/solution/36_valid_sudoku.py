# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
        """
        for i in range(9):
            visited = [False for _ in range(9)]
            for j in range(9):
                if board[i][j] != '.':
                    index = ord(board[i][j]) - ord('1')
                    if visited[index]:
                        return False
                    
                    visited[index] = True

            visited = [False for _ in range(9)]
            for j in range(9):
                if board[j][i] != '.':
                    index = ord(board[j][i]) - ord('1')
                    if visited[index]:
                        return False
                    
                    visited[index] = True

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                visited = [False for _ in range(9)]

                for k in range(3):
                    for h in range(3):
                        if board[i + k][j + h] != '.':
                            index = ord(board[i + k][j + h]) - ord('1')
                            if visited[index]:
                                return False

                            visited[index] = True

        return True