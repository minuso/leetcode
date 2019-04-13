def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    sum_ab = {}
    for a in A:
        for b in B:
            if a+b in sum_ab: sum_ab[a+b] += 1
            else: sum_ab[a+b] = 1
    res = 0
    for c in C:
        for d in D:
            if -(c+d) in sum_ab:
                res += sum_ab[-(c+d)]
    return res