def romanToInt(self, s):
    sym = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        
    n = 0
    pre, cur = 1000, 1000
    for c in s:
        cur = sym[c]
        n += cur
        if cur > pre:   # means addition of previous loop is wrong
            n -= pre*2  # substract twice to correct
        pre = cur
    return n