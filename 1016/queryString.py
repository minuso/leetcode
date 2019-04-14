def queryString(self, S: str, N: int) -> bool:
    return all(bin(n)[2:] in S for n in range(N, N//2, -1)) # [N/2,N] must contain [1,N/2]