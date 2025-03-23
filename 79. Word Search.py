from typing import List

class Solution:
    def isValid(self, grid, row, col) -> bool:
        rows, cols = len(grid), len(grid[0])
        return True if 0 <= row < rows and 0 <= col < cols else False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False]*cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                     # found the starting cell
                     if self.findWord(board, row, col, visited, 0, word):
                         return True
        return False

    def findWord(self, board, row, col, visited, idx, word) -> bool:
        if idx == len(word)-1:
            return True

        visited[row][col] = True
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for i in range(4):
            nrow, ncol = row + dirs[i][0], col + dirs[i][1]
            if self.isValid(board, nrow, ncol) and not visited[nrow][ncol] and board[nrow][ncol] == word[idx+1]:
                if self.findWord(board, nrow, ncol, visited, idx+1, word):
                    return True
        visited[row][col] = False
        return False

