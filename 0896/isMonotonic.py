def isMonotonic(self, A: List[int]) -> bool:
    if len(A) < 3: return True
        
    d = 1 if A[-1] - A[0] > 0 else -1
    for i in range(len(A) - 1):
        if (A[i+1] - A[i])*d < 0:
            return False
    return True