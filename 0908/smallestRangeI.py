def smallestRangeI(self, A: List[int], K: int) -> int:
    return max(0, max(A) - min(A) - K*2)