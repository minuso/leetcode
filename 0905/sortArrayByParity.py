def sortArrayByParity(self, A: List[int]) -> List[int]:
    l, r = 0, len(A) - 1
    while l < r:
        while l < r and A[l] & 1 == 0: l += 1 # l < r is better than l < len(A)
        while l < r and A[r] & 1 == 1: r -= 1 # l < r is better than r >= 0
        A[l], A[r] = A[r], A[l]               # swap directly: no need to check l and r in each iteration
                                              # (l < r is checked above, and l == r means the last iteration)
        l, r = l+1, r-1
    return A