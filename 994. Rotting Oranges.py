from collections import deque
from typing import List

class Pair:
    def __init__(self, row, col, time):
        self.row = row
        self.col = col
        self.time = time

class Solution:
    def isValid(self, grid, row, col) -> bool:
        rows, cols = len(grid), len(grid[0])
        return True if 0 <= row < rows and 0 <= col < cols else False

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visited = [[False] * cols for _ in range(rows)]
        fresh_orange_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_orange_count += 1
                elif grid[r][c] == 2:
                    q.append(Pair(r, c, 0))
                    visited[r][c] = True

        # Multi-Source BFS
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        time_to_rot = 0
        while q:
            pair = q.popleft()
            row, col, time = pair.row, pair.col, pair.time
            time_to_rot = max(time_to_rot, time)

            for i in range(4):
                nrow, ncol = row + dirs[i][0], col + dirs[i][1]
                if self.isValid(grid, nrow, ncol) and not visited[nrow][ncol] and grid[nrow][ncol] == 1:
                    q.append(Pair(nrow, ncol, time + 1))
                    visited[nrow][ncol] = True
                    fresh_orange_count -= 1

        return time_to_rot if fresh_orange_count == 0 else -1

if __name__ == "__main__":
    s = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(s.orangesRotting(grid2))
