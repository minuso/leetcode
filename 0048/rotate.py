def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    f, b = 0, n - 1
    while f < b:
        ul, ur, bl, br = f, f, b, b
        for _ in range(n - f*2 - 1): # minus 1: the position of near corner
            matrix[f][ul], matrix[ur][b],  \
            matrix[bl][f], matrix[b][br] = \
            matrix[bl][f], matrix[f][ul],  \
            matrix[b][br], matrix[ur][b] 
            ul, ur, bl, br = ul+1, ur+1, bl-1, br-1 # move to the near position
        f, b = f+1, b-1 # move to the inner layer