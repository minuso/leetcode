def shiftingLetters(self, S, shifts):
    ORD_LOWER_A = ord('a')
        
    res, sh = list(S), sum(shifts)
    for i in range(len(S)):
        res[i] = unichr(((ord(res[i]) -  ORD_LOWER_A + sh) % (26) + ORD_LOWER_A))
        sh -= shifts[i]
    return ''.join(res)