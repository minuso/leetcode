def minPathSum(self, grid: List[List[int]]) -> int:
    if not grid: return 0
        
    m, n = len(grid), len(grid[0])
    cur = [grid[0][0]] + [0]*(n-1)
    for i in range(1, n):
        cur[i] = cur[i-1] + grid[0][i]
    for i in range(1, m):
        cur[0] += grid[i][0]
        for j in range(1, n):
            cur[j] = min(cur[j-1], cur[j]) + grid[i][j] # select the min sum in [left, top] 
    return cur[-1]