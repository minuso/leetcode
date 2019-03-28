def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    is_even = [1 - (n&1) for n in A]
    even_sum = 0
    for i, n in enumerate(A): even_sum += n*is_even[i]
        
    res = []
    for [val, i] in queries:
        A[i] += val
        from_even = is_even[i]
        to_even = is_even[i] = 1 - (A[i]&1)
            
        if to_even:
            even_sum += val if from_even else A[i]
        elif from_even:                 # from even to odd: need minus previous A[i],
            even_sum -= (A[i] - val)    # which is even and had been added to even_sum
        res.append(even_sum)
    return res