def mySqrt(self, x):
    if x in [0, 1]: return x
        
    l, r = 1, x//2 # sqrt of x>1 must less than or equal to x/2
    while l <= r:
        m = (l + r) >> 1
        if m*m <= x < (m+1)*(m+1):
            return m
            
        if m*m < x:
            l = m + 1
        else:
            r = m