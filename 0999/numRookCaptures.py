def numRookCaptures(self, board: List[List[str]]) -> int:
    W_ROOK, EMPTY, B_PAWN = 'R', '.', 'p'
    N = len(board)
        
    def rookXY(board):
        for x in range(N):
            for y in range(N):
                if board[x][y] == W_ROOK:
                    return x, y
        return -1, -1
        
    x, y = rookXY(board)
    h, v = board[x], [board[i][y] for i in range(N)]
    l = [c for c in h[0:y][::-1] if c != EMPTY]
    r = [c for c in h[y+1:N] if c != EMPTY]
    u = [c for c in v[0:x][::-1] if c != EMPTY]
    d = [c for c in v[x+1:N] if c != EMPTY]
    return sum([1 for m in [u, d, l, r] if m and m[0] == B_PAWN])