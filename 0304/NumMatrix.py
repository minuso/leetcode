class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        
        self.sums = matrix # sum from (0,0) to (i,j)
        for i in range(1, len(self.sums[0])): self.sums[0][i] += self.sums[0][i-1]
        for i in range(1, len(self.sums)): self.sums[i][0] += self.sums[i-1][0]
        for i in range(1, len(self.sums)):
            for j in range(1, len(self.sums[0])):
                self.sums[i][j] += self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.sums[row2][col2]
        if row1 > 0: 
            res -= self.sums[row1 - 1][col2] # subtract top rectangle
        if col1 > 0: 
            res -= self.sums[row2][col1 - 1] # subtract left rectangle
        if row1*col1: 
            res += self.sums[row1 - 1][col1 - 1] # add top-left rectangle back
        return res