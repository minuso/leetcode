def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    h2ks = {}
    for [h, k] in people:
        if h in h2ks: h2ks[h].append(k)
        else: h2ks[h] = [k]
    for h in h2ks: h2ks[h].sort() # from less to more
            
    res = people
    remained = [i for i in range(len(res))]
    for h in sorted(h2ks.keys()): # from lower to higher
        same_h = 0 # same height
        for k in h2ks[h]:
            res[remained[k - same_h]] = [h, k]
            remained.pop(k - same_h)
            same_h += 1
    return res