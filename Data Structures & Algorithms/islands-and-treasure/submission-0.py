from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set() # (r, c)

        # find all gate
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        def addCell(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                grid[r][c] == -1 or (r, c) in visited):
                return
            visited.add((r, c))
            q.append((r, c))

        dist = 0
        # BFS at same time
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                # all direction
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1