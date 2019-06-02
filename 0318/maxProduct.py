def maxProduct(self, words: List[str]) -> int:
    BASE = ord('a')
        
    d = {}
    for w in words:
        mask = 0
        for c in set(w):
            mask |= (1 << (ord(c) - BASE))
        d[mask] = max(d.get(mask, 0), len(w))
    # use AND operation to check if duplicated
    return max([d[x]*d[y] for x in d for y in d if not x & y] or [0])