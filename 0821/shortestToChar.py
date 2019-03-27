def shortestToChar(self, S: str, C: str) -> List[int]:
    res = []
    cs = [] # indices of C in S 
    for i, c in enumerate(S):
        if c == C:
            res.append(0)
            cs.append(i)
        else:
            res.append(float('inf'))

    if not cs: return res
    
    for i in range(cs[0]): res[i] = cs[0] - i                   # leftmost
    for i in range(1, len(res) - cs[-1]): res[cs[-1] + i] = i   # rightmost
    if len(cs) > 1:
        start, end = 0, 1                                       # between two Cs
        while end != len(cs):
            l, r = cs[start]+1, cs[end]-1
            while l <= r: 
                res[l] = res[r] = res[l-1] + 1 # equal to res[r+1] + 1
                l, r = l+1, r-1
            start, end = start+1, end+1
    return res