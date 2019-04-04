def divide(self, dividend: int, divisor: int) -> int:
    if (dividend == -2147483648 and divisor == -1): return 2147483647 # overflow
    IS_POS = (dividend > 0) == (divisor > 0)
        
    remaind, UNIT = abs(dividend), abs(divisor)
    res = 0
    for x in range(32)[::-1]: # binary division
        if (remaind >> x) >= UNIT:
            res += (1 << x)
            remaind -= (UNIT << x)
    return res if IS_POS else -res