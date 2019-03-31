def baseNeg2(self, N: int) -> str:
    if N == 0: return "0"
        
    res = ""
    while N != 0:
        res = str(N % 2) + res # store the remainder
        if N % 2: # an odd number divided by -2 cause error: 5//(-2) = floor(-2.5) = -3 
            N -= 1
        N //= (-2)
    return res