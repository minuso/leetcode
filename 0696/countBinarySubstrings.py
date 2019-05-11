def countBinarySubstrings(self, s):
    res, pre, cur = 0, 0, 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cur += 1
        else:
            pre, cur, = cur, 1 
        res += (pre >= cur) # pre is sufficient to compose a binary string
    return res