def islandPerimeter(self, grid):
    res = 0
    top = [0]*len(grid[0])
    for row in grid:
        pre = 0
        for i, cur in enumerate(row):
            if cur == 1:
                res -= top[i]*2
                if pre == 0: res += 4
                else: res += 2
            top[i], pre = cur, cur
    return res