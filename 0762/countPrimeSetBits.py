def countPrimeSetBits(self, L: int, R: int) -> int:
    PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29} # limit of int set bits
    res = 0
    for n in range(L, R+1):
        if bin(n).count('1') in PRIMES:
            res += 1
    return res