def myPow(self, x: float, n: int) -> float:
    if n == 0: return 1
    if n < 0: return 1/self.myPow(x, -n)
        
    res = 1.0
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res