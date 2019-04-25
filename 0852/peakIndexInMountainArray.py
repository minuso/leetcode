def peakIndexInMountainArray(self, A: List[int]) -> int:
    l, r = 0, len(A) - 1
    while l < r:
        m = (l + r) >> 1
        if A[m] < A[m+1]:   # left slope
            l = m
        elif A[m-1] > A[m]: # right slope
            r = m
        else:
            return m