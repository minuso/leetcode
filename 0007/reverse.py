def reverse(self, x):
    n = abs(x)
    res = 0
    while n > 0:
        res = res*10 + n%10
        n //= 10
            
    if res > 2**31 - 1: return 0 # overflow
    return res if x > 0 else -res