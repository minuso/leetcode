def climbStairs(self, n):
    res = [[1, 0], 
           [0, 1]]
    A = [[1, 1], # fab_n+1, fab_n
         [1, 0]] # fab_n, fab_n-1
        
    def multiply(a, b):
        return [[a[0][0]*b[0][0]+a[0][1]*b[1][0], a[0][0]*b[0][1]+a[0][1]*b[1][1]], 
                [a[1][0]*b[0][0]+a[1][1]*b[1][0], a[1][0]*b[0][1]+a[1][1]*b[1][1]]]
        
    while n: 
        if n & 1:
            res = multiply(res, A)
        A = multiply(A, A)
        n >>= 1
    return res[0][0]