def maxScoreSightseeingPair(self, A: List[int]) -> int:
    res, max_start = 0, 0
    for i, v in enumerate(A):
        res = max(res, v - i + max_start) # max_start = A[i] + i
        max_start = max(max_start, v + i) # update the max-start spot for spots following
    return res