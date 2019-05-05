def largeGroupPositions(self, S: str) -> List[List[int]]:
    res = []
    cur_c, cur_start = '', 0
    for i, c in enumerate(S + 'E'): # add an end character (non-lowercase)
        if c != cur_c:
            if i - cur_start >= 3:
                res.append([cur_start, i-1])
            cur_c, cur_start = c, i
    return res