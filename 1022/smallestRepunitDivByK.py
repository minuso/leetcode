def smallestRepunitDivByK(self, K: int) -> int:
    if K%2 == 0 or K%5 == 0: return -1 # for speed up
        
    r = 1 # remainder
    for l in range(1, K+1): # r must in [0,K-1]
        if r % K == 0:
            return l
        r = (r*10 + 1) % K
    return -1 # after K tests, r must fall into the loop