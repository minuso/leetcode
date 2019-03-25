def diStringMatch(self, S: str) -> List[int]:
    l, r = 0, len(S) # two-pointer
    res = []
    for c in S:
        if c == 'I':      # if the next option is 'I'
            res.append(l) # put the smallest number
            l += 1
        else:
            res.append(r) # and vise versa
            r -= 1
    res.append(l) # do not forget the last number!
    return res