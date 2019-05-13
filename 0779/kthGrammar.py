def kthGrammar(self, N, K):
    if K == 1: return 0
    # N is useless
    # Kth symbol is generated from the (K+1)/2 th symbol of previous row
    # the pre-cur mapping is 0 -> 01 and 1 -> 10, 
    # which can be computed using 1-K%2 and K%2 separately
    return K%2 if self.kthGrammar(0, (K+1) >> 1) else 1 - K%2