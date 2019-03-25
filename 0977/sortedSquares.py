def sortedSquares(self, A: List[int]) -> List[int]:
    l, r = 0, len(A) - 1
    res = []
    while l <= r:
        if abs(A[l]) > abs(A[r]):
            res.append(A[l]*A[l])
            l += 1
        else:
            res.append(A[r]*A[r])
            r -= 1
    return res[::-1]