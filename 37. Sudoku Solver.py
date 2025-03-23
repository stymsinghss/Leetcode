from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self, board) -> bool:
        # Find empty cell
        empty_cell = self.findEmptyCell(board)
        if not empty_cell:
            return True

        row, col = empty_cell
        for i in range(1, 10):
            if self.canFill(board, row, col, str(i)):
                board[row][col] = str(i)
                if self.solve(board):
                    return True
                board[row][col] = "."
        return False

    def canFill(self, board, row, col, val) -> bool:
        # Check row and col
        for i in range(9):
            if board[row][i] == val or board[i][col] == val:
                return False

        # Check 3*3 subgrid
        start, end = (row // 3)*3, (col // 3)*3
        for i in range(3):
            for j in range(3):
                if board[start + i][end+j] == val:
                    return False

        return False

    def findEmptyCell(self, board):
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == ".":
                    return (row, col)
        return None



