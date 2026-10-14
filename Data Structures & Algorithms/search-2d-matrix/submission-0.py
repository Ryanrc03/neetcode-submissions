class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # find rows 
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]: # targer < x
                bot = row - 1
            elif target > matrix[row][-1]: # targer > y
                top = row + 1
            else:
                break
        # find item 
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[row][mid]: 
                r = mid - 1
            elif target > matrix[row][mid]: 
                l = mid + 1
            else:
                return True
        return False
