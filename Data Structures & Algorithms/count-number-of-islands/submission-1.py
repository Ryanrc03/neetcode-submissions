class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited set
        # dfs 
        res = 0 
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return False
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c):
                    res += 1
        return res