from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        time = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1: # 
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1
            print(grid)
        return time if fresh == 0 else -1