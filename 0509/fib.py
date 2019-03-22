def square2MatMul(self, A, B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0]), (A[0][0]*B[0][1]+A[0][1]*B[1][1])], 
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0]), (A[1][0]*B[0][1]+A[1][1]*B[1][1])]]
                    
def fib(self, N: int) -> int:
    if N in [0, 1]: return N
        
    A = [[1, 1], 
         [1, 0]]
    #fab = [[1], # 1st & 2nd terms of fab
    #       [0]]
        
    N -= 1
    An = [[1, 0], 
          [0, 1]]
    while N:
        if N & 1:
            An = self.square2MatMul(An, A)
        A = self.square2MatMul(A, A)
        N >>= 1
    return An[0][0] # (An*fab)[0][0] is equals to An[0][0] 