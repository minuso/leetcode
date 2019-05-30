def isValidSudoku(self, board: List[List[str]]) -> bool:
    BOARD_W, GRID_W = 9, 3
        
    def isUnique(nums):
        nums = [n for n in nums if n != '.']
        return len(nums) == len(set(nums))
        
    if not all([isUnique(row) for row in board]):
        return False
    if not all([isUnique(col) for col in zip(*board)]):
        return False
        
    for r in range(0, BOARD_W, GRID_W):
        for c in range(0, BOARD_W, GRID_W):
            grid = [board[r+i][c+j] for i in range(GRID_W) for j in range(GRID_W)]
            if not isUnique(grid):
                return False
    return True