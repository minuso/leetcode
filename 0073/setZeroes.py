def setZeroes(self, matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
                    
    for i in rows:
        for j in range(n):
            matrix[i][j] = 0
    for i in range(m):
        for j in cols:
            matrix[i][j] = 0